from __future__ import print_function
import logging

import requests
import phonenumbers
from tenacity import retry, wait_fixed, TryAgain


from config import CONFIG


headers = ({'Content-Type': 'application/x-www-form-urlencode'})
logger = logging.getLogger('bulksms')


def clean_msisdn(phone_number=None):
    """
    Clean mobile number
    :param phone_number: str
    :return: phone number representation including country code.
    """
    msisdn = phonenumbers.parse(phone_number)
    return int(str(msisdn.country_code) + str(msisdn.national_number))


@retry(wait=wait_fixed(2))
def send(msisdn=None, message=None):
    """
    Send SMS to any number in several countries.
    :param msisdn number. str
        The number to send to using international format.
    :param str message the message to be sent to msisdn.
    @return: Request results in pipe format [statusCode|statusString]
    """
    if not CONFIG.BULK_SMS.CLEAN_MOBILE_NUMBERS:
        msisdn = clean_msisdn(msisdn)

    payload = (
        {
            'username': CONFIG.get('BULK_SMS.AUTH.USERNAME', None),
            'password': CONFIG.get('BULK_SMS.AUTH.PASSWORD', None),
            'msisdn': msisdn,
            'message': message
        }
    )
    results = ''
    try:
        response = requests.post(CONFIG.BULK_SMS.URL.SINGLE, params=payload, headers=headers)
        if response.status_code < 200 or response.status_code >= 300:
            return 'Bad response status. {}'.format(response.status_code)
        results = response.content.split('|')
    except (requests.exceptions.Timeout, requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        logging.info(e)
        raise TryAgain
    except requests.exceptions.TooManyRedirects as e:
        return 'URL used was not correct, Please try another. {}'.format(e)
    except requests.exceptions.RequestException as e:
        logging.error('Catastrophic error occurred.', e)
    return results


def read_cvs(filename=None):
    """
    Read CVS File.
    """
    data = ""
    with open(filename) as file:
        for _ in file:
            data += _.replace("\"", "%22").replace("\n", "%0a").replace(" ", "+")
    return data


def send_bulk(filename=None):
    """
    Send bulk SMS.
    The API expects a passed CSV file to be
    in this format. receipent number & message:
    |-----------------------------------------|
      msisdn,message
      "27831234567","Message 1"
      "27831234566","Message 2"
    |-----------------------------------------|
     """
    api_credentials = CONFIG.get(CONFIG.AUTH, '')
    api_endpoint = CONFIG(CONFIG.BULK_SMS.URL.BATCH, '')
    results = ''
    try:
        url = api_endpoint+'?username='+api_credentials.USERNAME+'&password='+api_credentials.PASSWORD+'&batch_data='+read_cvs(filename)
        r = requests.get(url, headers=headers)
        if r.status_code < 200 or r.status_code >= 300:
            return "Bad response status"
        results = r.content.split('|')
    except requests.exceptions.Timeout:
        # TODO: Setup a retry or continue in retry loop
        return

    except requests.exceptions.TooManyRedirects:
        # TODO: URL used was not correct, Please try another
        return

    except requests.exceptions.RequestException as e:
        logging.error("Catastrophic error occurred.", e)
    return results
