import pandas as pd
import requests
from flask import Flask,jsonify,request,send_file, render_template,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import json



resp = requests.get('http://127.0.0.1:5000/sensor')

data = resp.json() 

print(data.json())

print(data['result'])

hash_montado = generate_password_hash(data['result'], method='sha256')

print(hash_montado)

print(data['hash'])

c = check_password_hash(data['hash'],hash_montado)

return jsonify({c})