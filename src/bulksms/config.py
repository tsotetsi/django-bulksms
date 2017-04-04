# BULKSMS Config.
CONFIG = {
    'BULK_SMS': {
        'AUTH': {
            'USERNAME': '',
            'PASSWORD': ''
        },
        'URL': {
            'SENDING': {
                {
                    'SINGLE': 'https://bulksms.2way.co.za/eapi/submission/send_sms/2/2.0',
                    'BATCH': 'https://bulksms.2way.co.za/eapi/submission/send_batch/1/1.0'
                }
            },
            'CREDITS': {
                'CREDITS': 'https://bulksms.2way.co.za/user/get_credits/1/1.1'
            }
        }
    },
    'CLEAN_MOBILE_NUMBERS': False
}
