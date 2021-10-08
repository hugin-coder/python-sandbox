from http.server import HTTPServer, BaseHTTPRequestHandler
import time

hostName = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __send(self, text):
        self.wfile.write(bytes(text, 'utf-8'))

    def do_GET(self):
        self.send_response(200, 'Garbage content')
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.__send('<h1>Hi :-)</h1>')
        self.__send(f'<p>Path: {self.path}</p>')
        self.__send(f'<p>Command: {self.command}</p>')
        self.__send(f'<p>Protocol version: {self.protocol_version}</p>')
        self.__send(f'<p>Request line: {self.requestline}</p>')
        # self.wfile.write(bytes("<h1>Hi :-)</h1>", "utf-8"))
        # self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        # self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        # self.wfile.write(bytes("<body>", "utf-8"))
        # self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        # self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200, 'Garbage content')
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print(self.rfile.readline(100))
        # self.__send(f'<p>Request: {self.request}</p>')


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
