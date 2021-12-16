from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
from user import User

@app.route('/')
def main_page():
    return render_template("newUserForm.html")

@app.route('/createUser', methods=["POST"])
def create_user():
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save_user(data)
    return redirect('/showusers')

@app.route('/showusers')
def show_users():
    users = User.get_all()
    print(users)
    return render_template("showUsers.html", users= users)

if __name__ == "__main__":
    app.run(debug=True)