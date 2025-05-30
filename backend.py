from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
api= Api(app)


import criptosistemas as resourcest
api.add_resource(resourcest.sustitucion, '/sustitucion/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)