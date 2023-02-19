import os

from flask import Flask

from db import db
from bp_api.views import api_blueprint
from bp_posts.views import posts_blueprint

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)

db.init_app(app)

if __name__ == "__main__":
    app.run(port=25000,
            debug=True)
