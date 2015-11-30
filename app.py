from flask import Flask, render_template, request, session, redirect, url_for
import user
import urllib2, json
import utils

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("Home.html")



if __name__ == "__main__":
    app.debug = True
    app.secret_key = "gP_3.hV[KE-P@|{pE5+Iv+m}"
    app.run('0.0.0.0', port=8000)
