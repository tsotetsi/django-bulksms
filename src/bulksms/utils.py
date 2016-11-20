from django.core.validators import RegexValidator


class E164Validator(RegexValidator):
    regex = r'^\+\d{11,15}$'
    message = "Number must comply to E.164 format. e.g '+27830000000' minimum 11 and maximum 15 digits."
