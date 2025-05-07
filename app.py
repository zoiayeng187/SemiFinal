import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Ayeng, Zoi Artchelo L. BSIT-||| B "

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT isn't set
    app.run(host='0.0.0.0', port=port)