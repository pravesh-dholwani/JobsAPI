from flask import Flask,jsonify,request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods = ['GET'])
def home():
    return jsonify({'data':"hello world"})

app.run()