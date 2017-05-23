# BULKSMS Configuration.

# Credentials required to use bulk sms api.
AUTH = {
    'username': '',
    'password': ''
}
# URL for sending single and batch sms.
URL_SENDING = {
    'batch': 'https://bulksms.2way.co.za/eapi/submission/send_batch/1/1.0',
    'single': 'https://bulksms.2way.co.za/eapi/submission/send_sms/2/2.0'
}

# URL for fetching credits balance.
URL_STATS = {
    'credits': 'https://bulksms.2way.co.za/user/get_credits/1/1.1'
}

# Whether to automatically insert country codes before sending sms.
CLEAN_MOBILE_NUMBERS = False
