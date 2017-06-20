# BULKSMS Configuration.

# BULKSMS base url.
BULKSMS_BASE_API_URL = 'https://bulksms.2way.co.za'

# Credentials required to use bulksms.com API.
BULKSMS_AUTH_USERNAME = ''
BULKSMS_AUTH_PASSWORD = ''

# URL for sending single and batch sms.
BULKSMS_API_URL = {
    'batch': '{}/eapi/submission/send_batch/1/1.0'.format(BULKSMS_BASE_API_URL),  # sends batch SMS's.
    'single': '{}/eapi/submission/send_sms/2/2.0'.format(BULKSMS_BASE_API_URL),  # sends single SMS.
    'credits': '{}/user/get_credits/1/1.1'.format(BULKSMS_BASE_API_URL),  # SMS credits balance.
    'inbox': '{}/reception/get_inbox/1/1.1'.format(BULKSMS_BASE_API_URL),  # get inbox.
    'quote': '{}/submission/quote_sms/2/2.0'.format(BULKSMS_BASE_API_URL)  # get sms quote.
}

# Whether to automatically insert country codes before sending sms.
CLEAN_MSISDN_NUMBER = False
