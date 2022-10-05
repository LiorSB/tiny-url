import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import date
# from pymongo import MongoClient



# mydatabase = client.TinyURLProject
# mycollection = mydatabase["URL"]
# print(client)
today = date.today().strftime("%m/%d/%Y")

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        response = json.dumps({"name": "this is tiny url7"})
        self.wfile.write(response.encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")
        self.end_headers()

    def do_POST(self):
        print(self.path)
        if (self.path == "/create-tiny-url"):
            print("create-tiny-url get request!")
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")
            self.end_headers()

            data_string = self.rfile.read(int(self.headers['Content-Length']))
            print(data_string)
            body = json.loads(data_string)
            response = json.dumps({"tinyUrl": body.get("srcUrl"), "srcUrl": body.get("srcUrl"),
                                   "creationDate": today})  # tinyurl: here need to call hash function for generate tinyUrl
            self.wfile.write(response.encode('utf-8'))
        if (self.path == "/get-original-url"):
            print("get-original-url get request!")
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")
            self.end_headers()

            data_string = self.rfile.read(int(self.headers['Content-Length']))
            print(data_string)
            body = json.loads(data_string)
            response = json.dumps({"tinyUrl": body.get("tinyUrl"), "srcUrl": body.get("tinyUrl"),
                                   "creationDate": today})  # tinyurl: here need to call hash function for generate tinyUrl
            self.wfile.write(response.encode('utf-8'))

def startServer(server_class=HTTPServer, handler_class=MyServer):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever(1.0)


startServer()
