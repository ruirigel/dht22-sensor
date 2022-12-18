#!/usr/bin/python3

# 20221027 Rui Rigel

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
import Adafruit_DHT
from dht22calcs import dewpoint, heatindex
import sys

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

hostName = "0.0.0.0"
serverPort = 8000

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
           if self.path == '/dht22values':
              humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
              t = round(temperature,1)
              rh = round(humidity,1)
              hi = round(heatindex(t,rh),1)
              self.send_response(200)
              self.send_header("Content-type", "text/plain")
              self.end_headers()
              self.wfile.write(bytes("{0},{1},{2:0.1f},{3:0.1f},{4},{5}".format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity, round(dewpoint(t,rh),1), round(heatindex(t,rh),1)), "utf-8"))

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
