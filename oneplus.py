import re

import tempmail

ACTIVATION_LINK_REGEX = 'https://account.oneplus.net/confirm/[0-9a-f]{32}'

NUMBER_OF_RETRIES = 100

def findActivationLink(emails):
	for email in emails:
		match = re.search(ACTIVATION_LINK_REGEX, email['mail_text'])
		if match:
			return match.group(0)

def getActivationLink(email_address):
	for attempt in xrange(NUMBER_OF_RETRIES):
		print 'Attempt %d for %s' % (attempt, email_address)
		emails = tempmail.getEmails(email_address)
		activation_link = findActivationLink(emails)

		if activation_link:
			return activation_link

	print 'Failed to get activation link for %s after %d retries' % (email_address, NUMBER_OF_RETRIES)
	return None

if __name__ == '__main__':
	print getActivationLink('weryujn7u@30wave.com')
