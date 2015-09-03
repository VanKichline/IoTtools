#!/usr/bin/python
# Based on:
#	http://www.acmesystems.it/python_httpd
#	https://pymotw.com/2/BaseHTTPServer/

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urlparse

PORT_NUMBER = 5050

class reqHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		parsed_path = urlparse.urlparse(self.path)
		q = urlparse.parse_qsl(parsed_path.query)

		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		
		# Send the html message
		result = self.process_query(q)
		self.wfile.write("Query Params:<br/>" + result)
		return
	
	# Dummy handler for processed query (list of name/value pairs)
	def process_query(self, query):
		return str(query)


#Create a web server and define the handler to manage the
#incoming request
try:
	server = HTTPServer(('', PORT_NUMBER), reqHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
