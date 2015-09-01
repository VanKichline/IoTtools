#!/usr/bin/python
# Based on: http://www.acmesystems.it/python_httpd

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080

class reqHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Hello World!")
		return


#Create a web server and define the handler to manage the
#incoming request
try:
	server = HTTPServer(('', PORT_NUMBER), reqHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
