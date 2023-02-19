import logging
from flask import Flask, request, render_template, send_from_directory

from bp_api.views import api_blueprint
from bp_posts.views import posts_blueprint

app = Flask(__name__)

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)

app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False


if __name__ == "__main__":
    app.run(debug=True)
