from flask import Flask
from flask import Flask, abort,  jsonify
from flask import request
import dredge
app = Flask(__name__)

@app.route("/getLastDocument")
def hello():
    items = dredge.getLastDocument()
    return jsonify(items)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)