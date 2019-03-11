import http.server
import socketserver
import termcolor


PORT = 8080



class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):


        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received
        print("  Command: " + self.command)

        # Print the resource requested
        print("  Path: " + self.path)

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