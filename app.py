from flask import Flask, url_for, redirect
from authlib.integrations.flask_client import OAuth
from datastax_astra import connect, insert_user
from flask import Flask
from datastax_astra import connect, insert_receipt, insert_food
import datetime

app = Flask(__name__)
app.secret_key = "much secret"
oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id="251887149747-5e5cf66kpqqdbst56s2mkc84php273r1.apps.googleusercontent.com",
    client_secret="2UaRM6NUi4ZU9oMDk_3lqqt0",
    access_token_url="https://accounts.google.com/o/oauth2/token",
    access_token_params=None,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params=None,
    api_base_url="https://www.googleapis.com/oauth2/v1/",
    userinfo_endpoint="https://openidconnect.googleapis.com/v1/userinfo",  # This is only needed if using openId to fetch user info
    client_kwargs={"scope": "openid email profile"},
)


@app.route("/")
def hello():
    connect()
    return f"Hello"


@app.route("/login")
def login():
    """Presents the Google login screen, user selects email and authorizes."""
    client = oauth.create_client("google")
    return client.authorize_redirect(url_for("authorize", _external=True))


@app.route("/authorize")
def authorize():
    """Extract user information.
    We can get name, email, profile picture, a unique id, and locale.
    """
    client = oauth.create_client("google")
    token = client.authorize_access_token()
    user_info = client.get("userinfo").json()
    insert_user(
        id=user_info["id"],
        first_name=user_info["given_name"],
        last_name=user_info["family_name"],
        profile_pic=user_info["picture"],
    )
    print(user_info)

    return redirect("/")


@app.route("/logout")
def logout():
    """Delete user data."""
    return redirect("/")


# @app.route("/")
def ReSpend(img):
    ### CONNECT TO DATABASE ###
    connect()

    ### GET TEXT FROM IMAGE ###

    ### STORE INFORMATION INTO DATABASE ###

    # receipt_id: current time
    receipt_id = datetime.datetime.now()

    # convert image to blob
    img_blob = 0

    # filter text for following info: vendor, total_spent, food items and corresponding prices
    vendor = ""
    total_spent = ""
    foods = {}
    # get category of each food
    category = ""
    units = 0
    for food in foods:
        total_spent = foods[food]
        insert_food(food, category, total_spent, units, receipt_id, user_info["id"])

    insert_receipt(img_blob, id, vendor, total_spent, user_info["id"])

    ### RETURN REQUESTED INFO ###


if __name__ == "__main__":
    app.run(debug=True)