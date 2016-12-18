import md5
import random
import requests
import string
import subprocess
import os
import json
DOMAINS = [
			'@30wave.com', '@fulvie.com', '@tverya.com', '@stromox.com',
			'@zainmax.net', '@9me.site', '@dr69.site', '@zain.site'
		]

USERNAME_CHARS = string.ascii_lowercase + string.digits
if os.path.exists("curl_command.txt"):
	BASE_URL = 'http://api.temp-mail.org/request'
else:
	BASE_URL = 'https://api.temp-mail.org/request'
	
GET_EMAILS_URL = BASE_URL + '/mail/id/%s/format/json/'
DELETE_EMAIL_URL = BASE_URL + '/delete/id/%s/format/json/'

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
	if os.path.exists("curl_command.txt"):
		f=open("curl_command.txt")
		command = f.read().strip()+" "+url
		process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		response_text = process.stdout.read()
		try:
			return json.loads(response_text)
		except:
			return []	
	url = GET_EMAILS_URL % md5_digest
	req = requests.get(url)

	if req.status_code == 200:
		return req.json()
	else:
		return []

def deleteEmail(mail_id):
	print 'trying deleting email %s' % mail_id

	url = DELETE_EMAIL_URL % mail_id
	if os.path.exists("curl_command.txt"):
		f=open("curl_command.txt")
		command = f.read().strip()+" "+url
		process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		response_text = process.stdout.read()
		try:
			json_ret = json.loads(response_text)
			if json_ret["result"] == "success":
				return True
			return False
		except:
			return False
	req = requests.get(url)
	status = req.status_code == 200 and req.json()['result'] == 'success'
	print 'deleted %s: %s' % (mail_id, status)
	return status

if __name__ == '__main__':
	x = 'cheop6vyn2@30wave.com'
	print getEmails(x)
