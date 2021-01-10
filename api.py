import sklearn
import joblib
from flask import Flask, jsonify,request
import pandas as pd


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.get_json(force=True)
    print(json_)
    query = pd.get_dummies(pd.DataFrame(json_))
    query = query.reindex(columns=model_columns, fill_value=0)

    prediction = list(lr.predict(query))

    for i in range(len(prediction)):
        if prediction[i]>0.5:
            prediction[i]=True
        else:
            prediction[i]=False
        print('prediction: is the message a spam?', str(prediction[i]))


    return jsonify({'prediction: Are/is this/these message(s) (a) spam(s)?': str(prediction)})

if __name__ == '__main__':
    lr = joblib.load(open('model.pkl','rb'))
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl")
    print ('Model columns loaded')

    app.run(port=5000, debug=True)