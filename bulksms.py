from __future__ import print_function

import requests

from config import url, url_batch, username, password


headers = ({'Content-Type':'application/x-www-form-urlencode'})


def clean_msisdn(number):
    pass


def send(msisdn, message):
    """
    Send SMS to any number in several countries.
    :param str msisdn number.
        The number to send to using international format.
    :param str message the message to be sent to msisdn.
    @return: Request results in pipe format [statusCode|statusString]
    """

    payload = ({'username':username,
                'password':password,
                'msisdn': clean_msisdn(msisdn),
                'message': message
               })

    try:
        r = requests.post(url, params=payload, headers=headers)

        if r.status_code < 200 or r.status_code >= 300:
            return "Bad response status"
        result = r.content.split('|')
    except requests.exceptions.Timeout:
        #TODO
        return "Setup a retry or continue in retry loop"

    except requests.exceptions.TooManyRedirects:
        return "URL used was not correct, Please try another"

    except requests.exceptions.RequestException as e:
        print("Catastrophic error occured", e)

    return result


def read_cvs(filename=None):
    """
    Read CVS File.
    """
    batch = ""
    with open(filename) as file:

        for line in file:
            batch += line.replace("\"","%22").replace("\n", "%0a").replace(" ","+")

    return batch


def send_bulk(filename=None):
    """
    Send bulk SMS.
     """
    try:
        url = url_batch+'?username='+username+'&password='+password+'&batch_data='+read_cvs(filename)
        r = requests.get(url, headers=headers)
        if r.status_code < 200 or r.status_code >= 300:
            return "Bad response status"
        result = r.content.split('|')
    except requests.exceptions.Timeout:
        #TODO
        return "Setup a retry or continue in retry loop"

    except requests.exceptions.TooManyRedirects:
        return "URL used was not correct, Please try another"

    except requests.exceptions.RequestException as e:
        return "Catastrophic error occured "+e
    return result
