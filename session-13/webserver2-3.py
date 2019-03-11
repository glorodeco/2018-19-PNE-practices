import http.server
import socketserver
import termcolor


PORT = 8001


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print("GET Received")

        termcolor.cprint(self.requestline, 'green')
        print("Request line:" + self.requestline)
        print("     Cnd:    " + self.command)
        print("Path:        " + self.path)


        if self.path == "/":
            with open("index.html", "r") as f:
                contents = f.read()
                f.close()
        else:
            with open("error.html", "r") as f:
                contents = f.read()
                f.close()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)


    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")