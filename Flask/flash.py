from flask import Flask,redirect,url_for,render_template,request,flash

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    return render_template('flash_index.html')

@app.route('/login',methods=['POST','GET'])
def login_in():
    error=None
    
    if request.method=='POST':
        if request.form['username']!='admin' or  request.form['password']!='admin':
            error="Invalid username and password"
        else:
            flash('you were sucessfully login')
            return redirect(url_for('index'))
        
    return render_template('flash_login.html',error=error)

 
if __name__=="__main__":
    app.run(debug=True)