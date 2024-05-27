import http.server
import socketserver
import json
import sqlite3

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path.startswith("/directory"):
            return self.consult()
        return super().do_GET()
    
    def consult(self):
        query = urlparse(self.path).query
        params = parse.qs(query)
        connection = sqlite3.connect("imdb.db")
        cursor = connection.cursor()

        if "actorId" in params:
            #Consulta pendiente
            response = ""
        elif "movieId" in params:
            #Consulta pendiente
            response = ""

        connection.close()

        self.send_header("Content-type", "application/josn")
        self.wfile.write(response)