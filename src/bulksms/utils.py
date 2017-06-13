import re

import phonenumbers

from .errors import InvalidMSISDNError


def clean_msisdn(phone_number):
    """
    Clean mobile number
    :param phone_number: str
    :return: phone number representation including country code.
    """
    msisdn = phonenumbers.parse(phone_number)
    return int(str(msisdn.country_code) + str(msisdn.national_number))


def read_cvs(filename):
    """
    Read CVS File.
    """
    data = ""
    with open(filename) as file:
        for _ in file:
            data += _.replace("\"", "%22").replace("\n", "%0a").replace(" ", "+")
    return data


def validate_msisdn_e164(mobile_number):
    pattern = re.compile('^\+\d{11,15}$')
    message = "Number must comply to E.164 format. e.g '+27830000000' minimum 11 and maximum 15 digits"
    if not re.match(pattern, mobile_number):
        raise InvalidMSISDNError(message=message)
    return mobile_number
