# Integrate HTML with Flask (Jinja2 Template)
# HTTP verb - GET and POST methods

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    return '<h2>The student has passed and the marks in percentage is </h2>' + str(score) + ' %'

@app.route('/fail/<int:score>')
def fail(score):
    return '<h2>The student has failed and the marks in percentage is </h2>' + str(score) + ' %'


@app.route('/results/<int:score>')
def  results(score):
    result = ''
    if score < 40:
        result = 'fail'
    else:
        result = 'success'

    return redirect(url_for(result, score=score))

# Result Checker
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = ''
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        english = float(request.form['english'])
        hindi = float(request.form['hindi'])
        total_score = (science+maths+english+hindi)/4

        res = ''
        if total_score >= 50:
            res = 'success'
        else:
            res = 'fail'

        return redirect(url_for(res, score=total_score))



if __name__ == '__main__':
    app.run(debug=True)