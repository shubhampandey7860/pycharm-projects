"""
The session can be defined as the duration for which a user logs into the server and logs out.
The data which is used to track this session is stored into the temporary directory on the server.


session[<variable-name>] = <value>   # creating session
session.pop(<variable-name>, none)   # removing session



"""

from flask import *

app = Flask(__name__)
app.secret_key = 'abc'


@app.route('/')
def home():
    res = make_response("<h1>session variable is set, <a href='/get'>Get Variable</a></h1>")
    session['response'] = 'session #1'
    return res


@app.route('/get')
def get_variable():
    if 'response' in session:
        s = session['response']
        return render_template("getSession.html", name=s)


if __name__ == '__main__':
    app.run(debug=True)
