from app import app
from flask import Flask,jsonify,request,send_file, render_template,jsonify
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from functools import wraps
from app import db
from app.models.tables import User



def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None

		if 'bi-access-token' in request.headers:
			token = request.headers['bi-access-token']

		if not token:
			return jsonify({'message' : 'Token is missing!'}),401

		try:
			data = jwt.decode(token, 'secret_token')
			current_user = User.query.filter_by(public_id=data['public_id']).first()
		except:
			return jsonify({'message' : 'Token is invalid!'}),401			

		return f(current_user, *args, **kwargs)

	return decorated



@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
	if not current_user.admin:
		return jsonify({'message' : 'You not the admin'})

	users = User.query.all()

	output = []

	for user in users:
		user_data = {}
		user_data['public_id'] = user.public_id
		user_data['name'] = user.name
		user_data['password'] = user.password
		user_data['admin'] = user.admin
		user_data['token'] = user.token
		output.append(user_data)

	return jsonify({'users' : output})



@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user,public_id):

	if not current_user.admin:
		return jsonify({'message' : 'You not the admin'})

	user = User.query.filter_by(public_id=public_id).first()

	if not user:
		return jsonify({'message' : 'No user found!'})

	db.session.delete(user)
	db.session.commit()

	return jsonify({'message' : 'The user has been deleted!'})



@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method='sha256')
	public_id = str(uuid.uuid4())

	token = jwt.encode({'public_id': public_id}, 'secret_token',  algorithm='HS256')

	new_user = User(public_id=public_id, name=data['name'], password=hashed_password,token=token.decode('UTF-8'), admin=True)
	
	db.session.add(new_user)
	db.session.commit()

	return jsonify({"message":"User Created!"})