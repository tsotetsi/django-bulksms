from __future__ import print_function
import logging

import requests
from tenacity import retry, wait_fixed, TryAgain


from settings import AUTH, CLEAN_MOBILE_NUMBERS, URL_SENDING
from utils import clean_msisdn, read_cvs


headers = ({'Content-Type': 'application/x-www-form-urlencode'})
logger = logging.getLogger('bulksms')

# API credentials
username = AUTH.get('username', None)
password = AUTH.get('password', None)


@staticmethod
@retry(wait=wait_fixed(2))
def send_single(msisdn, message):
    """
    Send SMS to any number in several countries.
    :param msisdn number. str
        The number to send to using international format.
    :param str message the message to be sent to msisdn.
    @return: Request results in pipe format [statusCode|statusString]
    """
    if not CLEAN_MOBILE_NUMBERS:
        msisdn = clean_msisdn(msisdn)

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
        response = requests.post(URL_SENDING.get('single', None), params=payload, headers=headers)
        if response.status_code < 200 or response.status_code >= 300:
            return 'Bad response status. {}'.format(response.status_code)
        results = response.content.split('|')
    except (requests.exceptions.Timeout, requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        logging.info(e)
        raise TryAgain
    except requests.exceptions.TooManyRedirects as e:
        return 'URL used was not correct, Please try another. {}'.format(e)
    except requests.exceptions.RequestException as e:
        logging.error('Catastrophic error occurred. ', e)
    return results


@staticmethod
def send_bulk(filename):
    """
    Send bulk SMS.
    The API expects a passed CSV file to be
    in this format. recipient number & message:4.

    Batch data is passed as query-parameter using
    an  HTTP get request.

    |-----------------------------------------|
      msisdn,message
      "27831234567","Message 1"
      "27831234566","Message 2"
    |-----------------------------------------|

     """
    api_endpoint = URL_SENDING.get('batch', None)
    results = ''
    try:
        url = api_endpoint+'?username='+username+'&password='+password+'&batch_data='+read_cvs(filename)
        response = requests.get(url, headers=headers)
        if response.status_code < 200 or response.status_code >= 300:
            return 'Bad response status. {}'.format(response.status_code)
        results = response.content.split('|')
    except (requests.exceptions.Timeout, requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        logging.info(e)
        raise TryAgain

    except requests.exceptions.TooManyRedirects as e:
        return 'Url used was not correct, Please try another. {}'.format(e)

    except requests.exceptions.RequestException as e:
        logging.error('Catastrophic error occurred.', e)
    return results
