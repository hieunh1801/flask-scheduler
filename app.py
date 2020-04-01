from flask import Flask
from mail_scheduler import scheduler

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    scheduler.start(paused=True)
    app.run(debug=True, port=5000)
