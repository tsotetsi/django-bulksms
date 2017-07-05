import re

import phonenumbers

from .errors import InvalidMSISDNError


def format_msisdn(phone_number):
    """
    format phone number
    :param phone_number: str
    :return: phone number representation including country code.
    """
    msisdn = phonenumbers.parse(phone_number)
    return int(str(msisdn.country_code) + str(msisdn.national_number))


def format_line(line):
    """
    Formats a line to required representation.
    :param line:
    :return: string url encoded.
    """
    if line:
        return line.replace("\"", "%22").replace("\n", "%0a").replace(" ", "+")


def read_cvs_file(filename):
    """
    Read CVS File.
    :param filename: str
    :return: file handler.
    """
    with open(filename) as file:
        return file


def process_cvs_file(file):
    """
    Process CVS file.
    :param file:
    :return:
    """
    data = ""
    for line in file:
        data += format_line(line)
    return data


def validate_msisdn_e164(mobile_number):
    pattern = re.compile('^\+\d{11,15}$')
    message = "Number must comply to E.164 format. e.g '+27830000000' minimum 11 and maximum 15 digits"
    if not re.match(pattern, mobile_number):
        raise InvalidMSISDNError(message=message)
    return mobile_number
