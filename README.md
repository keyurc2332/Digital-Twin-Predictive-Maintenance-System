# 🚀 Development of a Digital Twin-Based Predictive Maintenance System for Industrial Motors

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Backend-Flask-black?style=for-the-badge&logo=flask)
![ESP32](https://img.shields.io/badge/Hardware-ESP32-red?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![XGBoost](https://img.shields.io/badge/XGBoost-Classifier-orange?style=for-the-badge)
![Industry 4.0](https://img.shields.io/badge/Industry-4.0-blueviolet?style=for-the-badge)
![IoT](https://img.shields.io/badge/IoT-Enabled-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

## 📖 Overview

Traditional maintenance strategies either repair equipment **after failure** or service machines at fixed intervals regardless of their actual condition. This often results in unnecessary maintenance costs, unexpected equipment failures, production downtime, and reduced operational efficiency.

This project presents a **Digital Twin-Based Predictive Maintenance System** for industrial induction motors that combines **Industrial IoT**, **Machine Learning**, and an **interactive Digital Twin dashboard** to continuously monitor motor health in real time.

Sensor readings collected from the motor are processed through a multi-layer predictive maintenance pipeline consisting of anomaly detection, rule-based fault analysis, and machine learning-based fault classification. The processed information is visualized through an interactive dashboard that provides engineers with actionable insights including motor health, fault prediction, anomaly detection, maintenance recommendations, and Remaining Useful Life (RUL) estimation.

The project demonstrates how Digital Twin technology can be integrated with modern Industry 4.0 concepts to improve equipment reliability, reduce maintenance costs, and enable data-driven maintenance decisions.

---

## 🎯 Project Objectives

The primary objectives of this project are:

- Develop a Digital Twin of an industrial induction motor.
- Acquire real-time sensor data using ESP32 and IoT sensors.
- Detect abnormal operating conditions before equipment failure.
- Classify different motor fault conditions using Machine Learning.
- Estimate Remaining Useful Life (RUL) of the motor.
- Compute a real-time Motor Health Score.
- Provide maintenance recommendations based on sensor analytics.
- Visualize the complete system through an interactive dashboard.

---

# ✨ Key Features

## 🌐 Real-Time Motor Monitoring

- Continuous acquisition of sensor data
- Temperature monitoring
- Humidity monitoring
- Vibration monitoring
- RPM monitoring
- Live dashboard updates

---

## 🧠 Intelligent Machine Learning Pipeline

The predictive maintenance pipeline consists of multiple decision layers:

- Isolation Forest for anomaly detection
- Rule-Based Expert System
- XGBoost Multi-Class Fault Classifier
- Health Score Estimation
- Remaining Useful Life Prediction

---

## 🏭 Digital Twin Dashboard

Interactive dashboard displaying

- Motor Health Score
- Current Motor Status
- Predicted Fault Type
- Remaining Useful Life
- Live Sensor Values
- Vibration Analytics
- Temperature Trends
- Predictive Alerts
- Maintenance Recommendations
- Component Health Visualization

---

## ⚡ Industry 4.0 Architecture

The project integrates multiple Industry 4.0 technologies including

- Industrial IoT
- Digital Twin
- Edge Data Acquisition
- Machine Learning
- Real-Time Data Streaming
- Interactive Visualization

---

# 📸 Project Preview

> **Dashboard screenshots, Digital Twin visualization, hardware setup, and architecture diagrams will be added here.**

```
assets/screenshots/dashboard.png

assets/screenshots/digital_twin.png

assets/screenshots/hardware_setup.png

assets/demo/demo.gif
```

---

# 🚨 Problem Statement

Industrial induction motors operate continuously in manufacturing environments where unexpected failures can lead to production downtime, equipment damage, financial losses, and safety risks.

Traditional maintenance strategies suffer from several limitations:

- Reactive maintenance repairs machines only after failure.
- Preventive maintenance often replaces healthy components unnecessarily.
- Lack of continuous monitoring.
- No intelligent prediction of future failures.
- Limited visibility into equipment health.

There is a growing need for intelligent maintenance systems capable of continuously monitoring equipment, identifying abnormal behavior, and predicting failures before they occur.

---

# 💡 Proposed Solution

This project proposes a Digital Twin-Based Predictive Maintenance System capable of monitoring industrial motors in real time using IoT sensors and Machine Learning.

The complete system performs the following operations:

1. Collects sensor readings from the motor.
2. Streams data to the backend.
3. Extracts statistical features.
4. Detects anomalies.
5. Classifies fault types.
6. Computes Motor Health Score.
7. Estimates Remaining Useful Life.
8. Updates the Digital Twin Dashboard.
9. Generates maintenance recommendations.

The resulting system enables predictive maintenance instead of reactive maintenance, reducing downtime while improving equipment reliability.

---

# ⭐ Why This Project?

Unlike conventional motor monitoring systems, this project combines multiple technologies into a single integrated solution.

✔ Industrial IoT

✔ Digital Twin

✔ Machine Learning

✔ Real-Time Analytics

✔ Interactive Dashboard

✔ Predictive Maintenance

✔ Remaining Useful Life Estimation

✔ Health Score Calculation

✔ Explainable Maintenance Decisions

---

# 🏆 Highlights

- Real-time predictive maintenance platform
- Multi-layer machine learning architecture
- Interactive Digital Twin dashboard
- Industry 4.0 inspired system design
- End-to-end data acquisition and analytics pipeline
- Scalable architecture for future industrial deployment

---

# 🏗 System Architecture

The proposed system follows a layered Industry 4.0 architecture where physical sensor data is transformed into meaningful maintenance insights through Machine Learning and Digital Twin visualization.

```text
                    ┌──────────────────────────┐
                    │   Industrial Motor       │
                    └─────────────┬────────────┘
                                  │
                    Temperature • Vibration • RPM
                                  │
                    ┌─────────────▼────────────┐
                    │ ESP32 Data Acquisition   │
                    └─────────────┬────────────┘
                                  │
                        HTTP / MQTT Communication
                                  │
                    ┌─────────────▼────────────┐
                    │     Flask Backend        │
                    └─────────────┬────────────┘
                                  │
                  Feature Extraction & Processing
                                  │
                    ┌─────────────▼────────────┐
                    │ Machine Learning Engine  │
                    └─────────────┬────────────┘
                                  │
        Isolation Forest → Rule Engine → XGBoost
                                  │
                 Health Score • Fault Detection • RUL
                                  │
                    ┌─────────────▼────────────┐
                    │ Digital Twin Dashboard   │
                    └──────────────────────────┘
```

The modular architecture allows each component to operate independently while enabling seamless communication between hardware, backend services, machine learning models, and visualization modules.

---

# 🔄 End-to-End Workflow

The complete predictive maintenance pipeline consists of the following stages:

### Step 1 — Sensor Data Acquisition

The ESP32 continuously acquires real-time motor parameters including:

- Temperature
- Humidity
- Vibration (X, Y, Z)
- Motor RPM

↓

### Step 2 — Data Transmission

Sensor readings are streamed to the backend for processing.

↓

### Step 3 — Feature Engineering

The backend converts raw sensor values into statistical features such as:

- RMS
- Standard Deviation
- Kurtosis
- Skewness
- Peak-to-Peak Value
- Temperature Trend
- Vibration Magnitude

↓

### Step 4 — Anomaly Detection

Isolation Forest learns healthy motor behavior and identifies abnormal operating conditions.

↓

### Step 5 — Rule-Based Fault Detection

Domain knowledge is applied to identify strong fault signatures such as:

- Bearing Fault
- Rotor Fault
- Stator Fault
- Overheating

↓

### Step 6 — Machine Learning Classification

If required, the processed feature vector is passed to an XGBoost classifier to determine the most probable fault category.

↓

### Step 7 — Predictive Analytics

The backend computes:

- Motor Health Score
- Remaining Useful Life (RUL)
- Maintenance Recommendation
- Trend Analysis

↓

### Step 8 — Digital Twin Visualization

The interactive dashboard displays the complete motor state in real time.

---

# 📂 Repository Structure

```text
Digital-Twin-Predictive-Maintenance-System
│
├── assets/
│   ├── demo/
│   ├── icons/
│   ├── images/
│   └── screenshots/
│
├── backend/
│   ├── server.py
│   ├── csv_streamer.py
│   ├── config.py
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── models/
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   ├── style.css
│   ├── css/
│   ├── js/
│   └── models/
│
├── machine_learning/
│   ├── ml_pipeline.py
│   ├── evaluation/
│   ├── models/
│   ├── notebooks/
│   ├── preprocessing/
│   └── training/
│
├── datasets/
│
├── diagrams/
│
├── docs/
│
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# 🧰 Technology Stack

| Category | Technologies |
|------------|-------------|
| Programming Language | Python, JavaScript |
| Backend | Flask, Flask-CORS |
| Machine Learning | Scikit-Learn, XGBoost |
| Scientific Computing | NumPy, Pandas, SciPy |
| Frontend | HTML, CSS, JavaScript |
| Data Streaming | WebSockets |
| Communication | HTTP, MQTT Architecture |
| Hardware | ESP32 |
| Sensors | MPU6050, DHT11 |
| Visualization | Digital Twin Dashboard |
| Simulation | MATLAB |
| Development Tools | VS Code, Git, GitHub |

---

# 🧠 Machine Learning Pipeline

The Machine Learning module follows a multi-layer decision architecture designed to improve prediction reliability while minimizing false alarms.

```text
Raw Sensor Data
        │
        ▼
Feature Engineering
        │
        ▼
Isolation Forest
(Anomaly Detection)
        │
        ▼
Rule-Based Expert System
        │
        ▼
XGBoost Classifier
        │
        ▼
Health Score
        │
        ▼
Remaining Useful Life
        │
        ▼
Maintenance Recommendation
```

---

## Machine Learning Components

### Isolation Forest

Responsible for detecting abnormal operating conditions based on healthy motor behavior.

**Purpose**

- Learn normal operation
- Detect anomalies
- Reduce unnecessary fault classification

---

### Rule-Based Expert System

A knowledge-driven layer that evaluates sensor thresholds and known engineering conditions.

Examples include:

- Temperature threshold violations
- Excessive vibration
- Bearing degradation signatures
- Rotor imbalance

---

### XGBoost Multi-Class Classifier

Classifies abnormal operating conditions into different fault categories.

Supported fault classes include:

- Healthy
- Bearing Fault
- Stator Fault
- Rotor Fault
- Overheating

---

### Health Score Estimation

The system computes a real-time health score ranging from:

```text
0 ───────────────────────────────► 100

Critical                   Healthy
```

This score summarizes the overall operating condition of the motor.

---

### Remaining Useful Life (RUL)

The system continuously estimates the remaining operational life of the motor based on historical health degradation.

The RUL estimation assists maintenance engineers in scheduling preventive maintenance before catastrophic failures occur.

---

# 🌐 Backend Architecture

The backend acts as the central processing engine of the system.

Its responsibilities include:

- Receiving sensor data
- Feature engineering
- Running anomaly detection
- Executing machine learning models
- Computing health metrics
- Serving prediction APIs
- Streaming processed results to the dashboard

---

# 💻 Frontend Dashboard

The Digital Twin Dashboard provides operators with a real-time view of motor health.

Major dashboard components include:

- Motor Health Gauge
- Fault Classification
- Remaining Useful Life
- Temperature Monitoring
- Vibration Monitoring
- Live Sensor Charts
- Component Status
- Predictive Alerts
- Maintenance Recommendations

The interface continuously updates as new sensor readings are received from the backend.

---

# 🔁 Data Flow

```text
Motor
   │
Sensors
   │
ESP32
   │
Backend
   │
Feature Engineering
   │
Machine Learning
   │
Prediction
   │
Health Score
   │
Dashboard
   │
Maintenance Decision
```

---

# 📊 Project Results

The system was designed to demonstrate the feasibility of combining Industrial IoT, Digital Twin technology, and Machine Learning for predictive maintenance of industrial motors.

The implementation successfully performs:

- ✅ Real-time sensor monitoring
- ✅ Statistical feature extraction
- ✅ Anomaly detection
- ✅ Fault classification
- ✅ Health score computation
- ✅ Remaining Useful Life estimation
- ✅ Maintenance recommendation generation
- ✅ Interactive Digital Twin visualization

---

# 📈 Dashboard Capabilities

The dashboard provides operators with a centralized monitoring interface for the complete motor lifecycle.

| Feature | Description |
|---------|-------------|
| Motor Health Score | Overall motor condition (0–100) |
| Fault Detection | Current predicted fault category |
| Temperature Monitoring | Live motor temperature |
| Vibration Analytics | Real-time vibration magnitude |
| Humidity Monitoring | Environmental monitoring |
| Remaining Useful Life | Estimated operational life |
| Trend Analysis | Health degradation trend |
| Maintenance Tips | Intelligent recommendations |
| Component Status | Individual component monitoring |

---

# 🖼 Screenshots

> Screenshots will be added as the project evolves.

### Dashboard

```text
assets/screenshots/dashboard.png
```

---

### Digital Twin

```text
assets/screenshots/digital_twin.png
```

---

### Hardware Setup

```text
assets/screenshots/hardware_setup.png
```

---

### Machine Learning Results

```text
assets/screenshots/ml_pipeline.png
```

---

### System Architecture

```text
assets/screenshots/architecture.png
```

---

# 🎥 Demo

A complete demonstration of the project will be available here.

```text
assets/demo/demo.gif
```

or

```text
YouTube Demonstration Link
```

---

# 📂 Dataset

The project uses both real and simulated motor operating data.

The dataset contains parameters such as:

- Timestamp
- Temperature
- Humidity
- Acceleration (X)
- Acceleration (Y)
- Acceleration (Z)
- RPM
- Fault Labels

Example:

| Timestamp | Temp | Humidity | RPM |
|------------|------|----------|-----|
| 101220 | 42°C | 54% | 400 |

---

# 📋 Dataset Structure

```
datasets/

├── sample_dataset.csv

├── README.md

└── dataset_description.md
```

Only sample data is included in this repository. Large datasets are excluded to keep the repository lightweight.

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/Digital-Twin-Predictive-Maintenance-System.git

cd Digital-Twin-Predictive-Maintenance-System
```

---

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Backend

```bash
cd backend

python server.py
```

---

## CSV Streamer

```bash
python csv_streamer.py
```

---

## Frontend

Open

```
frontend/index.html
```

or serve the frontend using a local web server.

---

# ▶ Running the Project

The execution flow is as follows:

```text
Start Flask Backend

↓

Start CSV Streamer

↓

Open Dashboard

↓

Live Sensor Data

↓

Machine Learning Prediction

↓

Digital Twin Visualization
```

---

# 🌐 REST API

The backend exposes REST endpoints for sensor ingestion and prediction.

| Endpoint | Method | Purpose |
|-----------|--------|----------|
| `/status` | GET | Check backend status |
| `/ingest` | POST | Send sensor readings |
| `/predict` | GET | Get latest prediction |
| `/reset` | POST | Reset predictor state |

---

## Example Request

```json
POST /ingest

{
  "timestamp_ms": 17123456,
  "ax": 0.12,
  "ay": -0.02,
  "az": 9.81,
  "temp": 42.5,
  "humidity": 53,
  "rpm": 400
}
```

---

## Example Response

```json
{
  "health_score": 96.4,
  "fault_class": "None",
  "motor_status": "Healthy",
  "trend": "Stable",
  "rul_hours": 248,
  "maintenance_tip": "Lubrication not required yet"
}
```

---

# 🛠 Project Modules

## Hardware Layer

Responsible for collecting sensor readings from the motor.

### Components

- ESP32
- MPU6050
- DHT11
- Industrial Motor

---

## Data Acquisition Layer

Collects and transmits sensor values to the backend.

---

## Backend Layer

Processes incoming sensor data and performs:

- Feature Engineering
- Machine Learning
- Prediction
- Health Score Estimation

---

## Visualization Layer

Displays

- Digital Twin
- Live Charts
- Health Indicators
- Fault Information
- Predictive Analytics

---

# 📌 Folder Responsibilities

| Folder | Purpose |
|---------|----------|
| backend | Flask backend services |
| frontend | Dashboard application |
| machine_learning | ML models and pipeline |
| datasets | Sample datasets |
| docs | Project documentation |
| assets | Images, screenshots and demo |
| diagrams | Architecture diagrams |

---

# 🔍 Challenges Faced

Some of the key engineering challenges during development included:

- Processing noisy sensor data
- Designing a reliable anomaly detection pipeline
- Integrating multiple prediction layers
- Real-time dashboard synchronization
- Feature engineering for vibration analytics
- Remaining Useful Life estimation
- Balancing prediction accuracy with system responsiveness

---

# 📈 Future Enhancements

Potential future improvements include:

- Cloud deployment (AWS / Azure)
- Docker containerization
- Multi-motor monitoring
- OTA firmware updates
- Explainable AI (SHAP)
- Grafana dashboards
- Historical analytics database
- Mobile application
- Automated maintenance scheduling

> **Note:** These items represent planned future enhancements and are **not part of the current implementation**.

---

# 👥 Contributors

This project was developed as part of the Bachelor of Engineering (B.E.) Final Year Project.

| Name | Role |
|------|------|
| Keyur Chauhan | Machine Learning, Backend Development, System Integration |
| Shivangi Chouhan | Frontend Development, Documentation |
| Arshiya Khan | Hardware Integration, Testing |

> **Academic Guide:** Ms. Ekta Desai

---

# 🎓 Academic Information

**Project Title**

Development of a Digital Twin-Based Predictive Maintenance System for Industrial Motors

**Degree**

Bachelor of Engineering (B.E.)

**Department**

Internet of Things (IoT)

**Institution**

Thakur College of Engineering and Technology (TCET), Mumbai

**Academic Year**

2025–2026

---

# 🏆 Project Highlights

- End-to-end Industry 4.0 inspired architecture
- Digital Twin visualization for industrial motors
- Machine Learning based predictive maintenance
- Real-time sensor monitoring
- Multi-layer fault detection pipeline
- Remaining Useful Life (RUL) estimation
- Health Score computation
- Interactive monitoring dashboard
- Modular and extensible software architecture

---

# 📚 References

The implementation and design of this project were inspired by concepts from:

- Industry 4.0 and Digital Twin research
- Predictive Maintenance literature
- Machine Learning for Condition Monitoring
- XGBoost documentation
- Scikit-Learn documentation
- Flask documentation
- ESP32 documentation

Detailed references are available in the project report located in the `docs/` directory.

---

# 📖 Documentation

Additional project documentation can be found in:

```text
docs/

├── Final_Report.pdf

└── Project_Presentation.pdf
```

These documents provide detailed information about:

- Literature Review
- Methodology
- System Design
- Machine Learning Pipeline
- Experimental Results
- Future Scope

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a Pull Request.

For major changes, please open an issue first to discuss your proposed modifications.

---

# 📝 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

# 📜 Citation

If you use this project for academic purposes, please cite it as:

```text
Keyur Chauhan et al.

Development of a Digital Twin-Based Predictive Maintenance System for Industrial Motors.

Bachelor of Engineering Final Year Project

Thakur College of Engineering and Technology

2026
```

---

# 🙏 Acknowledgements

The successful completion of this project would not have been possible without the continuous guidance, encouragement, and support of our faculty members, project guide, institution, teammates, and everyone who contributed throughout the development process.

We sincerely thank all those who helped transform this idea into a working system.

---

# 📌 Repository Roadmap

### Version 1.0

- Digital Twin Dashboard
- Machine Learning Pipeline
- Flask Backend
- Real-Time Monitoring
- Fault Classification
- Remaining Useful Life Estimation

---

### Planned Improvements

- Cloud Deployment
- Multi-Motor Support
- Edge AI Optimization
- Historical Data Analytics
- Mobile Dashboard
- Explainable AI (SHAP)
- Docker Support
- CI/CD Pipeline

> These features represent future development plans and are **not part of the current implementation**.

---

# ⭐ Repository Statistics

GitHub automatically displays repository statistics including:

- ⭐ Stars
- 🍴 Forks
- 👀 Watchers
- 📝 Commits
- 📦 Releases

If you found this project interesting, consider giving it a ⭐.

---

# 📬 Contact

For questions, suggestions, or collaboration opportunities:

**Keyur Chauhan**

- GitHub: https://github.com/keyurc2332
- LinkedIn: *(Add your LinkedIn profile here)*

---

<div align="center">

## 🚀 Building Smarter Maintenance Systems Through IoT, Machine Learning, and Digital Twins

**If you found this repository useful, please consider giving it a ⭐.**

Made with ❤️ for Industrial IoT, Machine Learning, and Industry 4.0.

</div>
