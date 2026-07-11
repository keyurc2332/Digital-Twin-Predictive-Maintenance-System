"""
===========================================================
Development of a Digital Twin-Based Predictive Maintenance
System for Industrial Motors

Bachelor of Engineering Final Year Project

Institution:
Thakur College of Engineering and Technology (TCET)

Department:
Internet of Things (IoT)

Academic Year:
2025–2026

Authors:
- Keyur Chauhan
- Shivangi Chouhan
- Arshiya Khan

Guide:
Ms. Ekta Desai

Description:
Machine Learning pipeline responsible for feature
engineering, anomaly detection, fault classification,
health score estimation, and real-time predictive
maintenance.
===========================================================
"""

# NOTE:
# This file presents the core Machine Learning workflow used
# in the project. Supporting experimental scripts, model
# tuning notebooks, and auxiliary utilities have been
# intentionally omitted to keep the repository concise while
# demonstrating the primary implementation.

from collections import deque

import numpy as np
import pandas as pd

from scipy.stats import kurtosis, skew

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

from xgboost import XGBClassifier

# ==========================================================
# Dataset Loading
# ==========================================================


def load_all_data():
    """
    Load sample sensor dataset.

    Returns
    -------
    healthy_df : DataFrame
    full_df : DataFrame
    """

    data = pd.read_csv(
        "../datasets/sample_sensor_data.csv"
    )

    healthy_df = data[data["fault_label"] == 0].copy()

    return healthy_df, data


# ==========================================================
# Feature Engineering
# ==========================================================


def compute_features(
    dataframe,
    window_size=20
):
    """
    Compute statistical features over
    sliding windows.
    """

    features = []

    vibration = dataframe["az"].values

    for start in range(
        0,
        len(vibration) - window_size
    ):

        window = vibration[start:start + window_size]

        feature = {

            "mean": np.mean(window),

            "std": np.std(window),

            "max": np.max(window),

            "min": np.min(window),

            "rms": np.sqrt(
                np.mean(window ** 2)
            ),

            "skewness": skew(window),

            "kurtosis": kurtosis(window),

            "temperature":
                dataframe.iloc[start]["temp"],

            "humidity":
                dataframe.iloc[start]["humidity"],

            "fault_label":
                dataframe.iloc[start]["fault_label"]

        }

        features.append(feature)

    return pd.DataFrame(features)

# ==========================================================
# Anomaly Detection Model
# ==========================================================

def train_anomaly_detector(feature_df):
    """
    Train the Isolation Forest model using
    healthy operating conditions.

    Parameters
    ----------
    feature_df : DataFrame

    Returns
    -------
    isolation_model
    scaler
    feature_columns
    """

    feature_columns = [

        "mean",
        "std",
        "max",
        "min",
        "rms",
        "skewness",
        "kurtosis",
        "temperature",
        "humidity"

    ]

    X = feature_df[feature_columns]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    isolation_model = IsolationForest(

        n_estimators=300,

        contamination=0.03,

        random_state=42

    )

    isolation_model.fit(X_scaled)

    return isolation_model, scaler, feature_columns


# ==========================================================
# Fault Classification Model
# ==========================================================

def train_fault_classifier(feature_df):
    """
    Train the XGBoost classifier for
    fault prediction.

    Parameters
    ----------
    feature_df : DataFrame

    Returns
    -------
    classifier
    feature_columns
    """

    feature_columns = [

        "mean",
        "std",
        "max",
        "min",
        "rms",
        "skewness",
        "kurtosis",
        "temperature",
        "humidity"

    ]

    X = feature_df[feature_columns]

    y = feature_df["fault_label"]

    classifier = XGBClassifier(

        n_estimators=300,

        learning_rate=0.1,

        max_depth=5,

        random_state=42,

        eval_metric="mlogloss"

    )

    classifier.fit(X, y)

    return classifier, feature_columns


# ==========================================================
# Health Score Estimation
# ==========================================================

def calculate_health_score(
    anomaly,
    temperature,
    vibration
):
    """
    Estimate motor health score.

    Returns
    -------
    float
    """

    score = 100

    if anomaly:

        score -= 30

    score -= max(0, temperature - 35) * 2

    score -= vibration * 4

    score = np.clip(score, 0, 100)

    return round(score, 2)


# ==========================================================
# Remaining Useful Life (RUL)
# ==========================================================

def estimate_rul(health_score):
    """
    Estimate Remaining Useful Life.

    Returns
    -------
    int
    """

    if health_score >= 90:

        return 1500

    if health_score >= 75:

        return 1000

    if health_score >= 50:

        return 500

    return 200

# ==========================================================
# Real-Time Predictor
# ==========================================================

class RealTimePredictor:
    """
    Perform real-time predictive maintenance using
    incoming sensor readings.
    """

    def __init__(
        self,
        anomaly_model,
        scaler,
        classifier,
        anomaly_columns,
        classifier_columns,
        window_size=20
    ):

        self.anomaly_model = anomaly_model
        self.scaler = scaler
        self.classifier = classifier

        self.anomaly_columns = anomaly_columns
        self.classifier_columns = classifier_columns

        self.window_size = window_size

        self.sensor_buffer = deque(maxlen=window_size)

        self.latest_prediction = None

    # ------------------------------------------------------

    def add_reading(
        self,
        timestamp_ms,
        ax,
        ay,
        az,
        temp,
        hum,
        rpm=400
    ):
        """
        Add a new sensor reading to the rolling buffer.
        """

        self.sensor_buffer.append({

            "timestamp_ms": timestamp_ms,

            "ax": ax,

            "ay": ay,

            "az": az,

            "temp": temp,

            "humidity": hum,

            "rpm": rpm

        })

        if len(self.sensor_buffer) >= self.window_size:

            self.latest_prediction = self.predict()

    # ------------------------------------------------------

    def predict(self):
        """
        Execute the complete prediction pipeline.

        Returns
        -------
        dict
        """

        dataframe = pd.DataFrame(self.sensor_buffer)

        feature_df = compute_features(
            dataframe,
            self.window_size
        )

        latest = feature_df.iloc[-1]

        anomaly_input = pd.DataFrame([

            latest[self.anomaly_columns]

        ])

        anomaly_scaled = self.scaler.transform(
            anomaly_input
        )

        anomaly_result = self.anomaly_model.predict(
            anomaly_scaled
        )[0]

        anomaly = anomaly_result == -1

        classifier_input = pd.DataFrame([

            latest[self.classifier_columns]

        ])

        fault_prediction = int(

            self.classifier.predict(
                classifier_input
            )[0]

        )

        health_score = calculate_health_score(

            anomaly,

            latest["temperature"],

            latest["rms"]

        )

        rul = estimate_rul(
            health_score
        )

        recommendation = self.generate_recommendation(

            health_score,

            anomaly,

            fault_prediction

        )

        return {

            "health_score": health_score,

            "fault_prediction": fault_prediction,

            "anomaly_detected": anomaly,

            "remaining_useful_life": rul,

            "maintenance_recommendation": recommendation

        }

    # ------------------------------------------------------

    @staticmethod
    def generate_recommendation(
        health_score,
        anomaly,
        fault_prediction
    ):
        """
        Generate maintenance recommendation.
        """

        if anomaly:

            return "Immediate inspection recommended."

        if health_score < 50:

            return "Schedule maintenance as soon as possible."

        if health_score < 75:

            return "Monitor motor condition closely."

        if fault_prediction != 0:

            return "Potential fault detected. Perform preventive maintenance."

        return "Motor operating under normal conditions."

    # ------------------------------------------------------

    def get_ui_output(self):
        """
        Return latest prediction for dashboard.
        """

        return self.latest_prediction