# 20221027 Rui Rigel

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

hostName = "0.0.0.0"
serverPort = 8000

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
           # Specific name to show values
           if self.path == '/dht22values':
              humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
              self.send_response(200)
              self.send_header("Content-type", "text/plain")
              self.end_headers()
             # self.wfile.write(bytes("Date,Time,Temperature,Humidity\n", "utf-8"))
              self.wfile.write(bytes("{0},{1},{2:0.1f}*C,{3:0.1f}%".format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity), "utf-8"))
           # Specific name to show plot
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

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
