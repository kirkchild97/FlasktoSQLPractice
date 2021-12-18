from user_app import app
from flask import render_template, redirect, request, session, flash
from user_app.models.user import User


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

@app.route('/delete', methods=["POST"])
def delete_user():
    print(request.form["id"])
    data= {
        "id" : request.form["id"]
    }
    User.delete_user(data)
    return redirect('/showusers')

@app.route('/updateUser', methods=["POST"])
def update_user():
    data = {
        "id" : request.form["id"]
    }
    edit_user = User.get_user_by_id(data)
    if edit_user != False:
        return render_template("edituser.html", user = edit_user)
    else:
        return redirect('/showusers')

@app.route('/sendedits', methods=["POST"])
def confirm_edits():
    data = {
        "id" : request.form["id"],
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    print("Data to be Changed: ", data)
    User.update_user(data)
    return redirect('/showusers')