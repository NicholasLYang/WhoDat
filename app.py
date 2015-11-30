from flask import Flask, render_template, request
from utils import WhereSearch, WhoSearch, WhenSearch, WhySearch

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print request.form['query'][:3].lower()
        if request.form['query'][:3].lower() == "who":
            return render_template(
            'results.html',
            answer = WhoSearch(request.form['query']),
            questionstem = request.form['query'][3:-1]
            )
        if request.form['query'][:4].lower() =="when":
            return render_template(
            'results.html',
            answer = WhenSearch(request.form['query']),
            questionstem = " "
            )
    return render_template('home.html')


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "gP_3.hV[KE-P@|{pE5+Iv+m}"
    app.run('0.0.0.0', port=8000)
