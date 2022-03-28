import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from reader import File_Parser

HOST = "127.0.0.1"
PORT = 9000


class HTTP_Serv(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.dict = File_Parser.parse_csv()
        super().__init__(*args, **kwargs)

    def do_GET(self):

        card = self.path.split("/")[-1]
        if 16 <= len(card) <= 20 and card.isnumeric():
            try:
                bin_num = str(card)[:6]
                d = self.dict[bin_num]
                self.send_response(200, "OK")
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(d).encode("utf-8"))
            except KeyError:
                self.send_response(404, "No card")
                self.end_headers()

        else:
            self.send_response(500, "Incorrect card number")
            self.send_header("Content-type", "application/json")
            self.end_headers()


server = HTTPServer((HOST, PORT), HTTP_Serv)
print("Server running...")
server.serve_forever()
server.server_close()
