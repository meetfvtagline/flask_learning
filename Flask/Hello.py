from flask import Flask,url_for,redirect

app=Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Welcome To home page of Flask Application!"

def hello_flask():
    return "Hello from learn-flask!"
app.add_url_rule("/hello_flask","hello_flask",hello_flask)

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}, Welcome To learn-flask Application!"

@app.route("/hello/<name>/<int:age>")
def hello_name_age(name,age):
    return f"Hello, {name}, You are {age} years old. Welcome To learn-flask Application!"

@app.route("/hello/<name>/<float:score>")
def hello_name_score(name,score):
    return f"Hello , {name}, your score is {score}. Welcome To learn-flask Application!"

@app.route("/hello/admin_show")
def hello_admin_user():
    return "Hello Admin, Welcome To learn-flask Application!"

@app.route("/user/<username>")
def show_user_profile(username):
    if username=="admin":
        return redirect(url_for("hello_admin_user"))
    else:
        return redirect(url_for("hello_name",name=username))



if __name__=="__main__":
    app.run(debug=True)