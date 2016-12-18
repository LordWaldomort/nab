import os
import threading
import otp 
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urlparse

server_port = 8080;

curr_index=0
auth_list=[]

def readAuthList():
	global auth_list
	f=open("auth_list.txt")
	for line in f:
		auth_list+=[line.strip()]


class OTPServer(BaseHTTPRequestHandler):
        def do_GET(self):
        	global auth_list
		global curr_index
	        self.send_response(200)
                self.send_header('Content-type','text/html')
		self.send_header('Access-Control-Allow-Origin', '*');
                self.end_headers()
                method = self.path.split("?")[0]
                if method == "/get_auth":
                	self.wfile.write(auth_list[curr_index]);
			curr_index+=1
		elif method == "/request_otp":
			otp_text = otp.getOTP()
			self.wfile.write(otp_text)
		return


def startOTPServer():
        try:
                server = HTTPServer(('', server_port), OTPServer)
                server.serve_forever()
        except KeyboardInterrupt:
                print '^C received, shutting down the web server'
                server.socket.close()

if __name__ == '__main__':
	readAuthList()
        startOTPServer()
