from flask import Flask

app = Flask(__name__)


@app.route('/home/<username>')
def home(username):
    return f"hello {username}"


#  add_url_rule(<url rule>, <endpoint>, <view function>)

def Display(name):
    return f"Name:{name}"


app.add_url_rule("/display/<name>", "display/name", Display)

if __name__ == "__main__":
    app.run(debug=True)
