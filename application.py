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
    app.run(port=80,debug=True)