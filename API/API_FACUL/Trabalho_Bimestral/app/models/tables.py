from app import db



# class User(db.Model):
# 	__tablename__= "users"

# 	id = db.Column(db.Integer, primary_key=True)
# 	public_id = db.Column(db.String(50), unique=True)
# 	name = db.Column(db.String(50))
# 	password = db.Column(db.String(150))
# 	admin = db.Column(db.Boolean)
# 	token = db.Column(db.String(500))

# class User(db.Model):
# 	__tablename__ = "users"

  
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))

#     @property
#     def is_authenticated(self):
#     	return True    

#     @property
#     def is_activate(self):
#     	return True
    	
#     @property
#     def is_anonymous(self):
#     	return False

#     def get_id(self):
#     	retun str(self.id)

#     def __init__(self, email,password):
#     	self.email = email
#     	self.password = password		