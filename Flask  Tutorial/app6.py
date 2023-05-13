from flask import *


app = Flask(__name__)

@app.route('/Cookie')
def Set_Cookie():
    res = make_response("<h1>Cookie is set</h1>")
    res.set_cookie('Name',' Shubham Pandey')
    return  res



if __name__ == '__main__':
    app.run(debug=True)
