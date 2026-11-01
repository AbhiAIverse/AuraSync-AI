import sqlite3
import pandas as pd
from sklearn.linear_model import LogisticRegression
from core.database import DB_NAME, init_db

def predict_burnout_risk():
    """Analyzes historical session data using Scikit-Learn to predict burnout risk."""
    init_db()
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT duration_seconds, fatigue_alerts, bad_posture_count FROM sessions", conn)
    conn.close()
    
    if df.empty or len(df) < 2:
        return "Not enough data yet. Complete at least 2 sessions to run AI prediction!", "Low Risk"
        
    # Create target label: Burnout = high fatigue or long duration with high posture issues
    df['burnout'] = ((df['fatigue_alerts'] >= 2) | (df['bad_posture_count'] >= 3)).astype(int)
    
    X = df[['duration_seconds', 'fatigue_alerts', 'bad_posture_count']]
    y = df['burnout']
    
    # Handle edge case if all labels are identical
    if len(y.unique()) < 2:
        last_row = X.iloc[-1]
        if last_row['fatigue_alerts'] >= 2 or last_row['bad_posture_count'] >= 3:
            return "⚠️ Moderate-High Burnout Risk detected based on recent fatigue and posture spikes.", "Medium-High Risk"
        return "✅ Optimal Wellness State. Low burnout risk detected.", "Low Risk"
        
    # Train a lightweight Logistic Regression model
    model = LogisticRegression()
    model.fit(X, y)
    
    # Predict risk for the latest session
    latest_features = X.iloc[-1:].values
    prediction = model.predict(latest_features)[0]
    
    if prediction == 1:
        return "⚠️ High Burnout Risk Detected by ML Model! Your recent sessions show elevated fatigue and ergonomic strain. Consider taking a 15-minute break.", "High Risk"
    else:
        return "✅ Optimal Wellness State. Your focus and ergonomics are well-balanced according to AI telemetry.", "Low Risk"