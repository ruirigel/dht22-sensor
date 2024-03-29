#!/usr/bin/python3

# 20221027 Rui Rigel

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
from pathlib import Path
import sys

hostName = "0.0.0.0"
serverPort = 8000

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
           if self.path == '/dht22values':
              self.send_response(200)
              self.send_header("Content-type", "text/plain")
              self.end_headers()
              lastline = Path('plot.txt').read_text().splitlines()[-1]
              self.wfile.write(bytes("{0}".format(lastline), "utf-8"))

           elif self.path == "/favicon.ico":
                   iconame = self.path
                   iconame = iconame[1:]
                   iconfile = open(iconame, 'rb').read()
                   statinfo = os.stat(iconame)
                   iconsize = statinfo.st_size
                   self.send_response(200)
                   self.send_header("Content-type", "image/x-icon")
                   self.send_header("Content-length", iconsize)
                   self.end_headers()
                   self.wfile.write(iconfile)

           elif self.path == "/plot.png":
                   imgname = self.path
                   imgname = imgname[1:]
                   imgfile = open(imgname, 'rb').read()
                   statinfo = os.stat(imgname)
                   imgsize = statinfo.st_size
                   self.send_response(200)
                   self.send_header("Content-type", "image/png")
                   self.send_header("Content-length", imgsize)
                   self.end_headers()
                   self.wfile.write(imgfile)

           else:
                   self.send_response(442)
                   self.end_headers()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    buffer = 1
    sys.stderr = open('dht22server_log.txt', '+a', buffer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
