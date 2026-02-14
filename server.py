import sys
import http.server
import socketserver
import os

PORT = 8001

Handler = http.server.SimpleHTTPRequestHandler

# Ensure we are serving from the script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(f"--- STARTING SERVER ---", flush=True)

if not os.path.exists('index.html'):
    print("⚠️  WARNING: index.html not found!", flush=True)
    if os.path.exists('The Life Of Brian Krawitz.html'):
        print("ℹ️  Found 'The Life Of Brian Krawitz.html'. Rename it to 'index.html' to fix the directory listing.", flush=True)

# Try to find an open port
current_port = PORT
while current_port < PORT + 10:
    try:
        with socketserver.TCPServer(("", current_port), Handler) as httpd:
            httpd.allow_reuse_address = True
            print(f"✅ Serving at http://localhost:{current_port}", flush=True)
            print(f"   (Press Ctrl+C to stop)", flush=True)
            httpd.serve_forever()
        break
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"⚠️  Port {current_port} is busy. Trying {current_port + 1}...", flush=True)
            current_port += 1
        else:
            print(f"❌ Error: {e}", flush=True)
            break
    except KeyboardInterrupt:
        print("\nServer stopped.", flush=True)
        break