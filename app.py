from flask import Flask
from flask_cors import CORS
#from Services

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Abishai Test APIS are working'

