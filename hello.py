import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! It is another simple page for learn docker."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))  # port 5000 is the default
