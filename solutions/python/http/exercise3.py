"""
Exercise #3

Use the form in exercise3_form.html to trigger the request
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qsl


class myHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # POST
    def do_POST(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Gets the size of data
        l = int(self.headers.get("Content-length"))
        # Gets the data itself (byte string)
        vars = self.rfile.read(l)

        # Input parameters (as a dict)
        params = parse_qsl(vars)
        # Concatenate variable-value pairs into a single string
        msg = "".join(["{}: {}\n".format(p[0].decode("utf-8"), p[1].decode("utf-8")) for p in params])

        # Write message content as utf-8 data
        self.wfile.write(bytes(msg, "utf8"))
        return


def main():
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, myHTTPServer_RequestHandler)
    print("running server...")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
