from flask import Flask,jsonify,request,send_file, render_template,jsonify
import pandas as pd
import json
import os
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)



from app.controllers import index, users
from app.models import tables



