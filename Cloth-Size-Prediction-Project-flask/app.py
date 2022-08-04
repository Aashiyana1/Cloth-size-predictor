#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

# df = df.replace({'XXS':1, 'S':2,'M':3,'L':4,'XL':5,'XXL':6,'XXXL':7})
    output = round(prediction[0],2)
    if output<=1 :
        output="XXS"
    elif  output<=2:
        output="S"
    elif  output<=3:
        output="M" 
    elif  output<=4:
        output="L" 
    elif  output<=5:
        output="XL"       
    elif  output<=6:
        output="XXL"       
    else:
        output="XXXL"       
    

    return render_template('index.html', prediction_text='Size of cloth :{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True, port=5001)