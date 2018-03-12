"""
Exercise #1
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

class myHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Hello world!"
        # Write message content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

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

        # Write message content
        self.wfile.write(bytes("POST world!", "utf8"))
        self.wfile.write(vars)
        return


def main():
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, myHTTPServer_RequestHandler)
    print("running server...")
    httpd.serve_forever()

if __name__ == "__main__":
    main()