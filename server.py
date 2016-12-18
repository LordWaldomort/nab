import os
import threading

import oneplus
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urlparse

server_port = 8080;

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


class signUpServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write("<html><script>window.close();</script></html>");

		method = self.path.split("?")[0]
		if method == "/gen":
			email = urlparse.parse_qs(urlparse.urlparse(self.path).query).get("email", None)[0];
			print "Starting thread for ", email
			threading.Thread(target=getActivationLink, args=(email,)).start();
		return

def startSignupServer():
	try:
		server = HTTPServer(('', server_port), signUpServer)
		server.serve_forever()
	except KeyboardInterrupt:
		print '^C received, shutting down the web server'
		server.socket.close()

if __name__ == '__main__':
	#getActivationLink('weryujn7u@30wave.com')
	startSignupServer()
