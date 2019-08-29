import time
import BaseHTTPServer
from datetime import datetime
import pytz
import os

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 8000


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Basic HTML Server.</title></head>")
        s.wfile.write("<body><p>Exibiting basic system info.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".

	tz_BR = pytz.timezone('America/Sao_Paulo')
	now = datetime.now(tz_BR)
        s.wfile.write("<p>The time is: %s</p>" % now)

	fileup = open("/proc/uptime","r")
	uptime = fileup.read().split(' ')[0]
	s.wfile.write("<p>Uptime: %s</p>" % uptime)

	filecpu = open("/proc/cpuinfo", "r")
	cpuinfo = filecpu.read().split('\n')
	s.wfile.write("<p>%s</p>" % cpuinfo[4])
	s.wfile.write("<p>%s</p>" % cpuinfo[6])
	
	filestat = os.popen("iostat").read().split(' ')
	while("" in filestat): filestat.remove("")
	cpuuti = int(filestat[12],10) + int(filestat[13],10)
	s.wfile.write("<p>CPU utilization percentage: %s</p>" % cpuuti)

	filemem = open("/proc/meminfo").read().split('\n')
	s.wfile.write("<p>%s</p>" % filemem[0])
	s.wfile.write("<p>%s</p>" % filemem[1])

	filever = open("/proc/version").read()
	s.wfile.write("<p>System Version: %s</p>" % filever)

	fileps = os.popen("ps | tr -s ' ' | cut -d' ' -f2,4 | sed 's/^/\<\/br\>/g'").read()
	s.wfile.write("<p>Running Processes %s</p>" % fileps)

        s.wfile.write("</body></html>")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

