import http.server
import socketserver
import termcolor
from SeqP1 import Seq

PORT = 8081


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- Printing the request line
        reqpath = self.path
        termcolor.cprint(reqpath, 'blue')

        if reqpath.startswith('/seq?'):
            f = open('response.html', 'r')
            contents = f.read()
            sep = reqpath[5:].split('&')
            msg = ""
            chk = ""
            base = ""
            operation = ""
            for elem in sep:
                var = elem.split('=')
                if var[0] == 'msg':
                    msg = var[1]
                elif var[0] == 'chk':
                    chk = var[1]
                elif var[0] == 'base':
                    base = var[1]
                elif var[0] == 'operation':
                    operation = var[1]
            seq = Seq(msg)

            if msg== "":
                f = open('seqerror.html', 'r')
                contents = f.read()
                contents = contents.replace("#error#", 'The sequence introduced is not correct.')

            for basis in msg:
                if basis != 'A' and basis != 'C' and basis != 'G' and basis != 'T':
                    f = open('seqerror.html', 'r')
                    contents = f.read()
                    contents = contents.replace("#error#", 'The sequence introduced is not correct.')

            contents = contents.replace("#seq#", str(seq))
            if chk == 'on':
                seq_length = seq.len()
                contents = contents.replace("#len#", str(seq_length))
            else:
                contents = contents.replace("Length: ", '').replace("#len#", '')
            contents = contents.replace("#basis#", base)
            if operation == 'perc':
                perc_base = seq.perc(base)
                contents = contents.replace("#op#", 'percentage').replace("#result#", str(perc_base))
            elif operation == 'count':
                count_base = seq.count(base)
                contents = contents.replace("#op#", 'count').replace("#result#", str(count_base))

        elif reqpath == '/' or reqpath == '/seq':
            f = open("form.html", 'r')
            contents = f.read()

        else:
            f = open("error.html", 'r')
            contents = f.read()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))

        return


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT:  {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped")