from app import app
from flask import Flask,jsonify,request,send_file, render_template,jsonify
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
def index():
	return "Bem vindo a API_BI"


# @app.route("/teste",methods=['POST'])
# def teste():
# 	data = request.get_json()
# 	return jsonify(data)	

@app.route("/login")
def main():
	return render_template('login.html')

@app.route("/base.html")
def base():
	return render_template('base.html')


@app.route("/teste.html")
def teste():
	return render_template('teste.html')	




# @app.route("/sensor",methods=['GET'])
# def sensor():
	
# 	f = open("arduino.txt", "r") 
# 	p = f.read()
# 	hashed_password = generate_password_hash(p, method='sha256')
# 	return jsonify({"result": p,
# 					"hash:" :  hashed_password })
	
