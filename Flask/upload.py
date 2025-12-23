from flask import Flask,redirect,render_template,url_for,request
from werkzeug.utils import secure_filename
import os

app=Flask(__name__)

@app.route('/upload')
def index():
    return render_template("upload.html")

@app.route("/uploader",methods=['POST','GET'])
def uplaoder():
    if request.method == 'POST':
        UPLOAD_FOLDER = 'uploads'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'



if __name__=="__main__":
    app.run(debug=True)