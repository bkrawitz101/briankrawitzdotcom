#!/bin/bash
echo "Starting local server at http://localhost:8000"
# Open browser in background after 1 second delay to ensure server is ready
(sleep 1 && open "http://localhost:8000") &
python3 -m http.server 8000