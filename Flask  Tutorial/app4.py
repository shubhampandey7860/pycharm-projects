from flask import *

app = Flask(__name__)


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        passwrd = request.form['pass']
        if uname == "ayush" and passwrd == "google":
            return "Welcome %s" % uname

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
