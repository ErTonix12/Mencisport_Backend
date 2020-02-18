from flask import Flask
from post import PostRepository
import json
app = Flask(__name__)


@app.route("/articles/")
def get_posts():
    return json.dumps(
        PostRepository().get_daily_posts()
        )
