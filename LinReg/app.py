from Regression import *
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify

datasetx = [
    -3.46,
    -1.78,
    -2.26,
    -1,
    -1.45,
    -1.5,
    -0.36,
    0.86,
    0.6,
    1.8,
    1,
    3.3,
    2,
    1,
    0,
    1.5,
]

datasety = [
    2.98,
    2.24,
    1.08,
    1,
    1.28,
    0.58,
    0.5,
    0.72,
    -0.78,
    -1.6,
    -1,
    -2.33,
    -1,
    0,
    0,
    -1.31,
]

regression_status = LR2(datasetx, datasety)
regression_status.LR2Essence()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_number = float(data['number'])
    result = regression_status.LR2PredictionX(input_number)
    return jsonify({'result': result})

    plt.scatter(datasetx, datasety)
    a = regression_status.slope
    b = regression_status.intercept

    y = a * x + b

    plt.plot(datasetx, result)
    plt.plot(y, x)
    plt.title("linear regression")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()
    plt.savefig("./static/Generated.jpg")



if __name__ == '__main__':
    app.run(debug=True)