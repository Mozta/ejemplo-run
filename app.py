from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

PORT = int(os.environ.get("PORT",8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=PORT)