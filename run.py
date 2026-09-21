import os
import sys
from app.app import app

if __name__ == '__main__':
    # Print clear message for the beginner user
    print("=" * 60)
    print("  Cryptography Algorithms Implementation Project Web Server")
    print("  Internship: Codec Technologies 1-Month Cyber Security")
    print("=" * 60)
    print("  Running locally at: http://127.0.0.1:5000/")
    print("  Press Ctrl+C to stop the server.")
    print("=" * 60)
    
    # Run the Flask app
    app.run(host='127.0.0.1', port=5000, debug=True)
