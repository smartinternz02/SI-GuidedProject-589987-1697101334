from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app. route ("/")
def Home():
    
    return render_template ("home.html" )
    
@flask_app.route("/index.html")
def index():
    return render_template("index.html") 

@flask_app.route("/predict", methods = ["POST"])
def predict():
    attr1 = request.form['attr1']
    attr2 = request.form['attr2']
    attr3 = request.form['attr3']
    attr4 = request.form['attr4']
    attr5 = request.form['attr5']
    attr6 = request.form['attr6']
    attr7 = request.form['attr7']
    float_features = [float(attr1),float(attr2),float(attr3),float(attr4),float(attr5),float(attr6),float(attr7)]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    
    return render_template("index.html",prediction_text="The University Score is {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)