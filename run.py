from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser, threading

ROOT = Path(__file__).resolve().parent
PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
url = f"http://127.0.0.1:{PORT}/index.html"
print(f"RY-L1390 Three.js server: {url}")
threading.Timer(0.8, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\\nServer stopped.")
    server.server_close()
