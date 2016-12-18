import re

import tempmail

EMAIL_ADDRESS = 'weryujn7u@30wave.com'

OTP_REGEX = 'Your verification code is ([0-9]{6}).'

NUMBER_OF_RETRIES = 100

def findOTP(emails):
	for email in emails:
		match = re.search(OTP_REGEX, email['mail_text'])
		if match:
			return match.group(1), email['mail_id']

def getOTP():
	for attempt in xrange(NUMBER_OF_RETRIES):
		print 'Attempt %d' % attempt
		emails = tempmail.getEmails(EMAIL_ADDRESS)

		if len(emails) > 1:
			print 'Warning: more than one mail present. Preferring latest first.'
			emails = sorted(emails, key=lambda email: email['mail_timestamp'], reverse=True)

		result = findOTP(emails)
		if result:
			otp, mail_id = result
			print 'Got OTP'
			# definitely delete the email
			while(not tempmail.deleteEmail(mail_id)):
				pass
			return otp

	print 'Failed to get otp after %d retries' % NUMBER_OF_RETRIES
	return None

if __name__ == '__main__':
	print getOTP()
