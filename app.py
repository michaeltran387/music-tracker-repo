from flask import Flask, redirect, render_template, request, url_for, session, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        flash("Login successful.", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in.", "info")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in.", "info")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out, {user}.", "info")
    session.pop("user", None)
    
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)