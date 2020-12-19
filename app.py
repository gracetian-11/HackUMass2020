from flask import Flask, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
from datastax_astra import connect

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
    name = session.get("name", None)
    return f"Hello {name}"


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
    session["email"] = user_info["email"]
    session["name"] = user_info["name"]
    print(user_info)
    return redirect("/")


@app.route("/logout")
def logout():
    """Delete user data."""
    for key in list(session.keys()):
        session.pop(key)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)