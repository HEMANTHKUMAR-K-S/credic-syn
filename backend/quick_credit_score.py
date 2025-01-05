import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

class QuickCreditScore:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        self.scaler = StandardScaler()

    def mock_training_data(self, n_samples=1000):
        np.random.seed(42)
        data = {
            'monthly_income': np.random.normal(5000, 1500, n_samples),
            'monthly_spend': np.random.normal(3000, 1000, n_samples),
            'utility_score': np.random.uniform(0, 1, n_samples),
            'social_score': np.random.uniform(0, 1, n_samples),
            'age': np.random.normal(35, 10, n_samples)
        }
        df = pd.DataFrame(data)

        df['risk_score'] = (
            (df['monthly_income'] > df['monthly_spend']) & 
            (df['utility_score'] > 0.7) & 
            (df['social_score'] > 0.6)
        ).astype(int)

        return df

    def train_quick_model(self):
        df = self.mock_training_data()
        X = df.drop('risk_score', axis=1)
        y = df['risk_score']

        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        return self

    def predict_risk(self, features_dict):
        features_df = pd.DataFrame([features_dict])
        scaled_features = self.scaler.transform(features_df)
        risk_prob = self.model.predict_proba(scaled_features)[0][1]
        feature_importance = dict(zip(features_dict.keys(), self.model.feature_importances_))

        return risk_prob, feature_importance
