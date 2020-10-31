from http.server import BaseHTTPRequestHandler, HTTPServer
class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        path = self.path
        if path == "/":
            path = "/index"

        try:
            file  = open(path +'.txt', 'r')
        except FileNotFoundError:
            file  = open("404.txt", 'r')

        message = file.read()
        file.close()
        self.wfile.write(bytes(message, "utf8"))
        return



server = HTTPServer(('127.0.0.1', 8081), myHandler)
server.serve_forever()
