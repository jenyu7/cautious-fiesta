from flask import Flask, render_template, request
from util import hor
app = Flask(__name__)

@app.route("/")
def hello_world():
    #print request.method
    #print request.args
    return render_template("form.html")

@app.route("/auth", methods = ['post', "get"])
def authorized():
    disp_name = request.form['NAME']
    m = int(request.form['month'])
    d = int(request.form['day'])
    disp_sign = hor.get_horoscope(m, d)
    return render_template("model_tmplt.html", title = "Welcome!", name = disp_name, z_sign = disp_sign)

if __name__ == "__main__":
    app.debug = True
    app.run()


