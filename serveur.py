import http.server
import socketserver

port = (80)

address = ("", int(port))

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print("Serveur demarré sur le port ", port)

httpd.serve_forever()
