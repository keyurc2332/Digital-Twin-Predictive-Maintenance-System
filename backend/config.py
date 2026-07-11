"""
---------------------------------------------------------
Development of a Digital Twin-Based Predictive Maintenance
System for Industrial Motors

File: config.py

Description:
Central configuration file for the Flask backend.
This file stores application-wide constants, server
configuration, machine learning parameters, and dataset
locations used throughout the project.

Authors:
Keyur Chauhan
Shivangi Chouhan
Arshiya Khan

Guide:
Ms. Ekta Desai

Institution:
Thakur College of Engineering and Technology (TCET)

Academic Year:
2025–2026
---------------------------------------------------------
"""

import os

# ==========================================================
# Flask Configuration
# ==========================================================

HOST = "0.0.0.0"
PORT = 5000
DEBUG = True

# ==========================================================
# Project Information
# ==========================================================

PROJECT_NAME = "Digital Twin Predictive Maintenance System"

API_VERSION = "v1.0"

# ==========================================================
# Dataset Configuration
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_DIRECTORY = os.path.join(
    BASE_DIR,
    "..",
    "datasets"
)

SAMPLE_DATASET = os.path.join(
    DATASET_DIRECTORY,
    "sample_sensor_data.csv"
)

# ==========================================================
# Sensor Configuration
# ==========================================================

WINDOW_SIZE = 20

SAMPLING_INTERVAL = 0.5      # seconds

DEFAULT_RPM = 400

# ==========================================================
# Machine Learning Parameters
# ==========================================================

RANDOM_STATE = 42

ISOLATION_FOREST_TREES = 300

XGBOOST_ESTIMATORS = 300

ANOMALY_THRESHOLD = -0.15

# ==========================================================
# Health Score Parameters
# ==========================================================

MAX_HEALTH_SCORE = 100

MIN_HEALTH_SCORE = 0

WARNING_THRESHOLD = 75

CRITICAL_THRESHOLD = 50

# ==========================================================
# Remaining Useful Life (RUL)
# ==========================================================

DEFAULT_RUL = 1500

# ==========================================================
# API Messages
# ==========================================================

SERVER_STARTED = (
    "Digital Twin Predictive Maintenance Backend Started."
)

BUFFERING_MESSAGE = (
    "Waiting for sufficient sensor readings..."
)

MODEL_READY = (
    "Machine Learning models initialized successfully."
)