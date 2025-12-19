from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def get_data():
    return render_template('students.html')

@app.route('/showdata', methods=['POST'])
def show_data():
    if request.method == 'POST':
        res=request.form
        return render_template('result_student.html', res=res)
    
if __name__ == '__main__':
    app.run(debug=True)