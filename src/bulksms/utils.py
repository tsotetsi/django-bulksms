from errors import InvalidMSISDNError
import re


def validate_msisdn_e164(mobile_number):
    pattern = re.compile('^\+\d{11,15}$')
    message = "Number must comply to E.164 format. e.g '+27830000000' minimum 11 and maximum 15 digits"
    if not re.match(pattern, mobile_number):
        raise InvalidMSISDNError(message=message)

    return mobile_number
