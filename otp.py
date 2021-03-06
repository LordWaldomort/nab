import json
import re

import tempmail

EMAIL_ADDRESS = 'agamoneplusverify@30wave.com'

OTP_REGEX = 'Your verification code is ([^\.]*)\.'

NUMBER_OF_RETRIES = 100

def findOTP(emails):
	for email in emails:
		match = re.search(OTP_REGEX, email['mail_text'])
		if match:
			m = match.group(1)

			if len(m) == 6:
				return m
			else:
				j = json.loads(m)
				return str(j['code'])

def getOTP():
	for attempt in xrange(NUMBER_OF_RETRIES):
		print 'Attempt %d' % attempt
		emails = tempmail.getEmails(EMAIL_ADDRESS)

		if len(emails) > 1:
			print 'Warning: more than one mail present. Preferring latest first.'
			emails = sorted(emails, key=lambda email: email['mail_timestamp'], reverse=True)

		otp = findOTP(emails)
		if otp:
			print 'Got OTP'
			# definitely delete the emails
			for email in emails:
				while(not tempmail.deleteEmail(email['mail_id'])):
					pass
			return otp

	print 'Failed to get otp after %d retries' % NUMBER_OF_RETRIES
	return None

if __name__ == '__main__':
	print getOTP()
