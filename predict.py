from flask import Flask
from flask import request
from flask import jsonify
import xgboost as xgb

import pickle

model_file = 'model_CC.bin'

with open(model_file, 'rb') as f_in:
  # X_test, model = pickle.load(f_in)
    dv, model = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['GET'])
def predict():
    customer = request.get_json()
   # y = customer.is_safe
    X = xgb.DMatrix(customer, model.y_pred)
    
  #  X_test =dv.transform([customer])
    X_test =dv.transform([X])
    #y_pred = model.predict(X_test)
    y_pred = model.predict(X_test)[:, 1]
    ans_yes = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(ans_yes)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

