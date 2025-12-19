from flask import Flask, jsonify, request, render_template
import config
import datetime
from src.utils import MedicalInsurance
import warnings
warnings.filterwarnings('ignore')

Obj = MedicalInsurance()

app = Flask(__name__) 

@app.route('/')
def employee():
    return render_template('prediction.html')

@app.route("/prediction_api", methods=["POST"]) 
def prediction_api():
    data = request.form
    print("data :", data)

    predicted_charges = Obj.predict_charges(data)
    return {"result": f"Predicted Medical insurance charges is: {predicted_charges}"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.FLASK_PORT_NUMBER)
