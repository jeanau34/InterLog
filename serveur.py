import http.server
import socketserver

port = input("Quel est le port du serveur ? : ")

address = ("", int(port))

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print("Serveur démarré sur le port ", port)

httpd.serve_forever()
