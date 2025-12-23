from flask import Flask,render_template,flash,request
from forms import ContactForm

app=Flask(__name__)
app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/contact',methods=['GET','POST'])
def contact():
    form=ContactForm()

    if request.method=='POST':
        if form.validate() == False:
            flash("All Field Are required")
            return render_template('contact.html',form=form)
        else:
            return render_template("success.html")
    elif request.method=='GET':
        return render_template('contact.html',form=form)
    
    # if form.validate_on_submit():
    #     return render_template("success.html")
    # return render_template('contact.html',form=form)


if __name__=="__main__":
    app.run(debug=True)