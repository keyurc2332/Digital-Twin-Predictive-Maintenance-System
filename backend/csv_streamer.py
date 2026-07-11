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
This module simulates real-time sensor data streaming by
reading records from a CSV file and sending them to the
Flask backend through REST API requests.

It is primarily used for testing and demonstrating the
Digital Twin dashboard without requiring live hardware.
===========================================================
"""

import time
import pandas as pd
import requests

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

CSV_FILE = "../datasets/sample_sensor_data.csv"

API_ENDPOINT = "http://127.0.0.1:5000/ingest"

STREAM_DELAY = 0.5  # seconds


# ---------------------------------------------------------
# CSV Streaming Function
# ---------------------------------------------------------

def stream_sensor_data():
    """
    Read sensor readings from a CSV file and stream them
    sequentially to the backend.
    """

    print("=" * 60)
    print(" Starting CSV Sensor Stream ")
    print("=" * 60)

    data = pd.read_csv(CSV_FILE)

    print(f"[INFO] Loaded {len(data)} sensor records.\n")

    for index, row in data.iterrows():

        payload = {

            "timestamp_ms": int(row["timestamp_ms"]),

            "ax": float(row["ax"]),

            "ay": float(row["ay"]),

            "az": float(row["az"]),

            "temp": float(row["temp"]),

            "humidity": float(row["humidity"]),

            "rpm": int(row["rpm"])

        }

        try:

            response = requests.post(
                API_ENDPOINT,
                json=payload,
                timeout=5
            )

            print(
                f"[{index + 1}] "
                f"Status: {response.status_code}"
            )

        except requests.exceptions.RequestException as error:

            print(
                f"[ERROR] Unable to send data: {error}"
            )

        time.sleep(STREAM_DELAY)

    print("\nStreaming completed successfully.")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    stream_sensor_data()