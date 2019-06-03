from app import app
from flask import Flask,jsonify,request,send_file, render_template,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import json
import hashlib

@app.route("/")
def index():
	return "Bem vindo a API_BI"




@app.route("/login")
def main():
	return render_template('login.html')

@app.route("/base.html")
def base():

	resp = requests.get('http://192.168.2.1:8080/')

	data = resp.json()

	conf_hash = data['hash'] 
	json_file = {}
	json_file['sen_1'] = data['sen_1']
	json_file['sen_2'] = data['sen_2']

	file = json.dumps(json_file, sort_keys = True).encode("utf-8")
	gera_hash= hashlib.md5(file).hexdigest()

	if(conf_hash == gera_hash):
		print("Hash confiavel")
	
	else:
		print("Hash não confiavel")

	sens_dado_1_0 = data['sen_1'][0]
	sens_dado_1_1 = data['sen_1'][1]
	sens_dado_1_2 = data['sen_1'][2]
	sens_dado_1_3 = data['sen_1'][3]
	sens_dado_1_4 = data['sen_1'][4]
	sens_dado_1_5 = data['sen_1'][5]
	sens_dado_1_6 = data['sen_1'][6]

	sens_dado_2_0 = data['sen_2'][0]
	sens_dado_2_1 = data['sen_2'][1]
	sens_dado_2_2 = data['sen_2'][2]
	sens_dado_2_3 = data['sen_2'][3]
	sens_dado_2_4 = data['sen_2'][4]
	sens_dado_2_5 = data['sen_2'][5]
	sens_dado_2_6 = data['sen_2'][6]


	# return jsonify(teste1)
	return render_template('base.html',sens_dado_1_0=sens_dado_1_0, sens_dado_1_1=sens_dado_1_1,sens_dado_1_2=sens_dado_1_2,sens_dado_1_3=sens_dado_1_3,sens_dado_1_4=sens_dado_1_4,sens_dado_1_5=sens_dado_1_5,sens_dado_1_6=sens_dado_1_6,sens_dado_2_0=sens_dado_2_0,sens_dado_2_1=sens_dado_2_1, sens_dado_2_2=sens_dado_2_2,sens_dado_2_3=sens_dado_2_3,sens_dado_2_4=sens_dado_2_4,sens_dado_2_5=sens_dado_2_5,sens_dado_2_6=sens_dado_2_6)

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
	
