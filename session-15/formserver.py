import http.server
import socketserver
import termcolor

PORT=8080;

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        #printing the request line

        termcolor.cprint(self.requestline, 'green')

        f =open ('form-2.html', 'r')
        contents = f.read()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html' )
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        #Send the body of the reponse message

        self.wfile.write(str.encode(contents))


# Main programme

with socketserver.TCPServer(("",PORT ), TestHandler) as httpd:
    print('Serving at PORT: {}'.format(PORT))


    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.server_close()

print('The server is stopped')


