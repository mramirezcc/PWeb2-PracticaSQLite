import http.server
import socketserver
import json
import sqlite3
from urllib.parse import urlparse, parse_qs

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path.startswith("/directory"):
            return self.consult()
        return super().do_GET()
    
    def consult(self):
        query = urlparse(self.path).query
        params = parse_qs(query)
        connection = sqlite3.connect("imdb.db")
        cursor = connection.cursor()

        if "actorId" in params:
            actorId = params["actorId"]
            cursor.execute("SELECT Movie.MovieID, Movie.Title, Movie.Year, Movie.Score, Movie.Votes FROM Movie\
                JOIN Casting ON Movie.MovieID = Casting.MovieID)\
                WHERE Casting.ActorI = ?", (actorId))
            data = cursor.fetchall()
            result = []
            for row in data:
                result.append({"movieId": row[0], "title": row[1], "year": row[2], "rating": row[3], "votes": row[4], "ordinal": row[5]})
        elif "movieId" in params:
            #Consulta pendiente
            result = []

        connection.close()

        self.send_header("Content-type", "application/josn")
        self.wfile.write(result)