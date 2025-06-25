import os
from flask import Flask
from flask_migrate import Migrate
from server.models import db

app = Flask(__name__)

# Absolute path to server/app.db
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
