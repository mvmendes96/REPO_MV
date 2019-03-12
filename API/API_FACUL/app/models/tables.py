from app import db



class User(db.Model):
	__tablename__= "users"

	id = db.Column(db.Integer, primary_key=True)
	public_id = db.Column(db.String(50), unique=True)
	name = db.Column(db.String(50))
	password = db.Column(db.String(150))
	admin = db.Column(db.Boolean)
	token = db.Column(db.String(500))


