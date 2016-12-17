import re
import requests

import tempmail

ACTIVATION_LINK_REGEX = 'https://account.oneplus.net/confirm/[0-9a-f]{32}'

NUMBER_OF_RETRIES = 100

def findActivationLink(emails):
	for email in emails:
		match = re.search(ACTIVATION_LINK_REGEX, email['mail_text'])
		if match:
			return match.group(0)

def activate(email_address):
	for attempt in xrange(NUMBER_OF_RETRIES):
		print 'Activation attempt %d for %s' % (attempt, email_address)
		emails = tempmail.getEmails(email_address)
		activation_link = findActivationLink(emails)

		if activation_link:
			req = requests.get(activation_link)
			if req.status_code == 200:
				print 'Activated %s' % email_address
				return True
			else:
				print 'Failed to activate %s via link %s' % (email_address, activation_link)
				return False

	return False

if __name__ == '__main__':
	print activate('weryujn7u@30wave.com')
