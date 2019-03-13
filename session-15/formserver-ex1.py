import http.server
import socketserver
import termcolor

PORT=8081;

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        if self.requestline=='GET / HTTP/1.1' or self.requestline== 'GET /echo HTTP/1.1':
        #printing the request line
            termcolor.cprint(self.requestline, 'green')

            f =open ('form-ex1.html', 'r')
            contents = f.read()

            self.send_response(200)

            self.send_header('Content-Type', 'text/html' )
            self.send_header('Content-Length', len(str.encode(contents)))

            self.end_headers()

            #Send the body of the reponse message
            self.wfile.write(str.encode(contents))
            # create an INET, STREAMing socket
            print(self.requestline)

        elif self.requestline=='GET /form-ex1.html HTTP/1.1':
            f = open('form-ex1.html', 'r')
            contents = f.read()

            self.send_response(200)

            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))

            self.end_headers()

            # Send the body of the reponse message
            self.wfile.write(str.encode(contents))
            # create an INET, STREAMing socket
            print(self.requestline)


        elif 'msg' in self.requestline:
            #print(self.requestline[14:-8])
            msg = self.requestline[14:-8]
            f = open('webresponse.html', 'r')
            contents = f.read()
            contents = contents.replace('patata', msg)
            self.send_response(200)

            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))

            self.end_headers()

            # Send the body of the reponse message

            self.wfile.write(str.encode(contents))
            # create an INET, STREAMing socket
            print(self.requestline[14:-8])

        else:
            f = open('error-ex1.html', 'r')
            contents = f.read()

            self.send_response(200)

            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))

            self.end_headers()

            # Send the body of the reponse message
            self.wfile.write(str.encode(contents))
            # create an INET, STREAMing socket
            print(self.requestline)



# Main programme

with socketserver.TCPServer(("",PORT ), TestHandler) as httpd:
    print('Serving at PORT: {}'.format(PORT))


    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.server_close()

print('The server is stopped')


