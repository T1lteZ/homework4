from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        self.send_response(200)
        if self.path.startswith("/src/img"):
            file_path = f"{self.path[5:]}"
            if file_path.endswith(".png"):
                if os.path.exists(file_path):
                    self.send_header("Content-type", "image/png")
                    self.end_headers()
                    with open(file_path, "rb") as file:
                        self.wfile.write(file.read())
            elif file_path.endswith("svg"):
                if os.path.exists(file_path):
                    self.send_header("Content-type", "image/svg+xml")
                    self.end_headers()
                    with open(file_path, "rb") as file:
                        self.wfile.write(file.read())
            else:
                self.send_error(404, "Image Not Found")

        if self.path == "/":
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(
                "C:/Users/Nurlan/IT/Проекты/django/html/contacts.html",
                "r",
                encoding="utf-8",
            ) as file:
                reader = file.read()
            self.wfile.write(bytes(reader, "utf-8"))
        elif self.path == "/catalog" or self.path == "/category" or self.path == "/contacts" or self.path == "/main":
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(
                f"C:/Users/Nurlan/IT/Проекты/django/html{self.path}.html",
                "r",
                encoding="utf-8",
            ) as file:
                reader = file.read()
            self.wfile.write(bytes(reader, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
