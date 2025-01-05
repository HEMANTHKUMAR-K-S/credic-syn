from flask import Flask, request, jsonify
from quick_credit_score import QuickCreditScore

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    score_model = QuickCreditScore()
    score_model.train_quick_model()
    
    risk_prob, feature_importance = score_model.predict_risk(data)
    
    return jsonify({'score': risk_prob * 100, 'feature_importance': feature_importance})

if __name__ == '__main__':
    app.run(debug=True)
