from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import hashlib
import json
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'storage.db')


bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                if form.email.data == "master@teste.com":
                    return redirect(url_for('dashboard'))
                else :
                    return redirect(url_for('dashboard_2'))

        return '<h1>Invalid email or password</h1>'

        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

    

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():

    resp = requests.get('http://192.168.2.1:8080/')

    data = resp.json()

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

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

@app.route('/dashboard_2')
@login_required
def dashboard_2():

    resp = requests.get('http://192.168.2.1:8080/')

    data = resp.json()

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

    conf_hash = data['hash'] 
    json_file = {}
    # json_file['sen_1'] = data['sen_1']
    json_file['sen_2'] = data['sen_2']

    file = json.dumps(json_file, sort_keys = True).encode("utf-8")
    gera_hash= hashlib.md5(file).hexdigest()

    if(conf_hash == gera_hash):
        print("Hash confiavel")
    
    else:
        print("Hash não confiavel")

    # sens_dado_1_0 = data['sen_1'][0]
    # sens_dado_1_1 = data['sen_1'][1]
    # sens_dado_1_2 = data['sen_1'][2]
    # sens_dado_1_3 = data['sen_1'][3]
    # sens_dado_1_4 = data['sen_1'][4]
    # sens_dado_1_5 = data['sen_1'][5]
    # sens_dado_1_6 = data['sen_1'][6]

    sens_dado_2_0 = data['sen_2'][0]
    sens_dado_2_1 = data['sen_2'][1]
    sens_dado_2_2 = data['sen_2'][2]
    sens_dado_2_3 = data['sen_2'][3]
    sens_dado_2_4 = data['sen_2'][4]
    sens_dado_2_5 = data['sen_2'][5]
    sens_dado_2_6 = data['sen_2'][6]


    # return jsonify(teste1)
    return render_template('base_2.html',sens_dado_2_0=sens_dado_2_0,sens_dado_2_1=sens_dado_2_1, sens_dado_2_2=sens_dado_2_2,sens_dado_2_3=sens_dado_2_3,sens_dado_2_4=sens_dado_2_4,sens_dado_2_5=sens_dado_2_5,sens_dado_2_6=sens_dado_2_6)




@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
     manager.run()
