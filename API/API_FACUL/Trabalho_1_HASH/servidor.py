from app import app
from flask import Flask,jsonify,request,send_file, render_template,jsonify
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/")
def index():
	return "Bem vindo a API_BI"


@app.route("/teste",methods=['POST'])
def teste():
	data = request.get_json()
	return jsonify(data)	



@app.route("/sensor",methods=['GET'])
def sensor():
	
	f = open("arduino.txt", "r") 
	p = f.read()
	hashed_password = generate_password_hash(p, method='sha256')

	

	return jsonify({"result": p,
					"hash:" :  hashed_password })
	
