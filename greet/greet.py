import json
import redis
from flask import Flask, request, render_template
from typing import Text, Optional, Dict, Any

app = Flask(__name__)


def get_current_user() -> Optional[Dict[Text, Any]]:
    """Extract current user details from storage."""

    red = redis.StrictRedis(host="redis", port=6379)
    encoded_user = red.get("user")
    if encoded_user:
        return json.loads(encoded_user)
    else:
        return None


def store_user(user: Dict[Text, Any]) -> None:
    """Save user details to our storage."""

    red = redis.StrictRedis(host="redis", port=6379)
    red.set("user", json.dumps(user))


@app.route('/', methods=["GET"])
def greet():
    """greet the user."""

    user = get_current_user()
    if user is not None:
        return "Hello, {}!".format(user.get("name"))
    else:
        # return render_tremplate()
        return "Hello, unknown stranger!"


@app.route('/', methods=["POST"])
def save_name():
    """Change a users details"""

    user = request.json
    print(user)
    store_user(user)
    return "I'll try to remember your name, {}!".format(user.get("name"))

@app.route('/about', methods=['Get','post'])
def about():
    pass


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)

