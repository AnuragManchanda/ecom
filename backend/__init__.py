from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from backend.migration import migrate
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema

import time
time.sleep(5)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysqldb/ecom'
db = SQLAlchemy(app)
migrate(db)
ma = Marshmallow(app)
