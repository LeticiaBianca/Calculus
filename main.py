from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

from Integral import integral

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    na = request.form['na']
    nb = request.form['nb']
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']

    result = integral(na,nb,a,b,c)

    return render_template('home.html', prediction_text = str(result))

if __name__ == '__main__':
    app.run()