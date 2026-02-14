## 🚀 Local Development Server (Required for 3D Models)

3D models only work over HTTP (not file://). Use Python's built-in server:

### Option 1: Run the Script (Easiest)

**Mac/Linux:**
```bash
./start_server.sh
```

**Windows:**
Double-click `start_server.bat` or run:
```cmd
start_server.bat
```

### Option 2: Manual Command
```bash
# Navigate to your portfolio folder
cd /path/to/your/portfolio

# Start server
python3 -m http.server 8000

# Visit in browser
http://localhost:8000
```