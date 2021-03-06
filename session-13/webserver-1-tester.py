import http.server
import socketserver

PORT = 8001

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('GET received')

        print('Request line: '+ self.requestline)
        print(' Cmd: ' + self.command)
        print(' Path: '+ self.path)

        content = 'I am the happy server! :-)'

        self.send_response(200);
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content- Lenght', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return



Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print('Serving in PORT', PORT)

    httpd.serve_forever()




