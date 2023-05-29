from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

from Integral import integral

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    da = request.form['da']
    db = request.form['db']
    numerador = request.form['numerador']
    denominador = request.form['denominador']

    result = integral(da,db,numerador, denominador)

    return render_template('home.html', prediction_text = result)

if __name__ == '__main__':
    app.run()