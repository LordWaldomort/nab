import md5
import random
import requests
import string

DOMAINS = [
			'@30wave.com', '@fulvie.com', '@tverya.com', '@stromox.com',
			'@zainmax.net', '@9me.site', '@dr69.site', '@zain.site'
		]

USERNAME_CHARS = string.ascii_lowercase + string.digits
GET_EMAILS_URL = 'http://api.temp-mail.org/request/mail/id/%s/format/json/'

def getMD5Digest(str):
	return md5.new(str).hexdigest()

def getRandomUsername(length=10):
	return ''.join(random.choice(USERNAME_CHARS) for _ in xrange(length))

def getRandomDomain():
	return random.choice(DOMAINS)

def getRandomEmailAddress():
	return getRandomUsername() + getRandomDomain()

def getEmails(email_address):
	md5_digest = getMD5Digest(email_address)
	url = GET_EMAILS_URL % md5_digest
	req = requests.get(url)

	if req.status_code == 200:
		return req.json()
	else:
		return []

if __name__ == '__main__':
	x = 'cheop6vyn2@30wave.com'
	print getEmails(x)
