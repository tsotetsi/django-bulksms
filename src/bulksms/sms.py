from __future__ import print_function
import logging

import requests
from tenacity import retry, wait_fixed, TryAgain

from django.conf import settings
from .utils import format_msisdn, read_cvs_file


headers = ({'Content-Type': 'application/x-www-form-urlencode'})
logger = logging.getLogger('bulksms')

# API Authentication credentials.
username = getattr(settings, 'BULKSMS_AUTH_USERNAME', '')
password = getattr(settings, 'BULKSMS_AUTH_PASSWORD', '')
api_url = getattr(settings, 'BULKSMS_API_URL', '')

# Whether to insert country codes or not.
clean_msisdn_number = getattr(settings, 'CLEAN_MSISDN_NUMBER', False)


@retry(wait=wait_fixed(2))
def send_single(msisdn=None, message=None):
    """
    Send SMS to any number in several countries.
    :param msisdn number. str
        The number to send to using international format.
    :param str message the message to be sent to msisdn.
    @return: Request results in pipe format [statusCode|statusString]
    """
    if clean_msisdn_number:
        msisdn = format_msisdn(msisdn)

    payload = (
        {
            'username': username,
            'password': password,
            'msisdn': msisdn,
            'message': message
        }
    )
    results = ''
    try:
        response = requests.post(api_url.get('single', None), params=payload, headers=headers)
        if response.status_code < 200 or response.status_code >= 300:
            return 'Bad request. {}'.format(response.status_code)
        results = response.content.split('|')
    except (requests.exceptions.Timeout, requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        logging.info(e)
        raise TryAgain
    except requests.exceptions.TooManyRedirects as e:
        return 'Invalid url. {}'.format(e)
    except requests.exceptions.RequestException as e:
        logging.error('Catastrophic error occurred. ', e)
    return results


def send_bulk(filename=None):
    """
    Send bulk SMS. The API expects a given CSV file to be in the format as show below.

    Batch data is passed as query-parameters using an  HTTP get request.

    |-----------------------------------------|
      msisdn,message
      "27831234567","Message 1"
      "27831234566","Message 2"
    |-----------------------------------------|
    :param filename :  contains a list of msisdn and message.
     """
    api_endpoint = api_url.get('batch', None)
    results = ''
    try:
        url = '{}?username={}&password={}&batch_data={}'.format(api_endpoint, username, password, read_cvs_file(filename))
        response = requests.get(url, headers=headers)
        if response.status_code < 200 or response.status_code >= 300:
            return 'Bad request: {}'.format(response.status_code)
        results = response.content.split('|')
    except (requests.exceptions.Timeout, requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        logging.info(e)
        raise TryAgain

    except requests.exceptions.TooManyRedirects as e:
        return 'Invalid url: {}'.format(e)

    except requests.exceptions.RequestException as e:
        logging.error('Catastrophic error occurred: ', e)
    return results
