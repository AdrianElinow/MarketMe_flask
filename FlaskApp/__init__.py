from flask import Flask
import json
app = Flask(__name__)
@app.route("/")
def hello():
    return """\
	{"gameID":"1"}\
"""
if __name__ == "__main__":
    app.run()
