
from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Containerization and Orchestration Lab</h1>
    <h2>Application is running successfully!</h2>
    <p>Container Hostname: {socket.gethostname()}</p>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
