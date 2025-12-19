from flask import Flask,render_template,render_template

app=Flask(__name__)

# @app.route("/hello/<user>")
# def index(user):
#     return render_template("hello.html",name=user)


# @app.route("/hello/<int:marks>")
# def marks(marks):
#     return render_template('hello.html',score=marks)

# if __name__=="__main__":
#     app.run(debug=True)

@app.route("/res")
def index():
    d={"name":"Meet","age":21,"city":"Ahmedabad"}
    return render_template("hello.html",valu=d)

if __name__=="__main__":
    app.run(debug=True)