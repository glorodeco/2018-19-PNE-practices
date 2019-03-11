import http.server
import socketserver


PORT = 8002


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print("GET received!")


        return


Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")

