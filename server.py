import os
import threading

import oneplus

ACTIVATION_LINK_FILENAME = 'activation_links.txt'

activation_link_file = open(ACTIVATION_LINK_FILENAME, 'a')

lock = threading.Lock()
def writeToFile(file, text):
	with lock:
		file.write(text)
		file.flush()
		os.fsync(file.fileno())


def getActivationLink(email_address):
	activation_link = oneplus.getActivationLink(email_address)

	if not activation_link:
		print 'Failed to get link for %s' % email_address
		return

	writeToFile(activation_link_file, '%s\t%s\n' % (email_address, activation_link))

def startServer():
	# TODO(ajay): write server stuff
	pass

if __name__ == '__main__':
	getActivationLink('weryujn7u@30wave.com')
