import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('C:/Users/A Kumar/Desktop/pr/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    bed = request.form.get("bed")
    bath = request.form.get("bath")
    sl = request.form.get("sl")
    sql = request.form.get("sql")
    fl = request.form.get("fl")
    w = request.form.get("w")
    v= request.form.get("v")
    c = request.form.get("c")
    g = request.form.get("g")
    sa = request.form.get("sa")
    sb = request.form.get("sb")
    yb = request.form.get("yb")
    yr = request.form.get("yr")
    z = request.form.get("z")
    sl15 = request.form.get("sl15")
    sq15 = request.form.get("sq15")


    
    pred=model.predict([[bed,bath,sl,sql,fl,w,v,c,g,sa,sb,yb,yr,z,sl15,sq15]])
    print(pred)
    
    
    #if pred < 0:
     #   return render_template('op.html', pred='Error calculating Amount!')
    #else:
    return render_template('op.html', pred='Expected amount is {}'.format(pred))


if __name__ == "__main__":
    app.run(debug=True)