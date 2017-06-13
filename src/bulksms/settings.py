# BULKSMS Configuration.

# Credentials required to use bulksms.com API.
BULKSMS_AUTH_USERNAME = ''
BULKSMS_AUTH_PASSWORD = ''

# URL for sending single and batch sms.
BULKSMS_API_URL = {
    'batch': 'https://bulksms.2way.co.za/eapi/submission/send_batch/1/1.0',  # sends batch SMS's.
    'single': 'https://bulksms.2way.co.za/eapi/submission/send_sms/2/2.0',  # sends single SMS.
    'credits': 'https://bulksms.2way.co.za/user/get_credits/1/1.1'  # SMS credits balance.
}

# Whether to automatically insert country codes before sending sms.
CLEAN_MSISDN_NUMBER = False
