from flask import Flask,jsonify,request,send_file, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route("/",methods=['POST'])
def hello():
	data = request.get_json()

	x = data["numero_1"]
	y = data["numero_2"]
	op = data["operação"]

	if(op == '+'):
		result = x + y

	if(op == '-'):
		result = x - y

	if(op == '*'):
		result = x * y

	if(op == '/'):
		if(y == 0):
			return jsonify({"Numero_2": "invalido"})
		result = x / y	

	else:
		return jsonify({"operação": "invalido"})

	return jsonify({"Resultado": result})	

if __name__ == '__main__':
	app.run(debug=True)


