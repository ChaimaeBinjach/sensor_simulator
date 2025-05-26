# 🌡️ Sensor Simulator for IoT Devices

This project is a Python script that simulates temperature and humidity data from multiple IoT sensors and sends it to an InfluxDB time-series database. The data can be visualized in real-time using Grafana dashboards, which makes it ideal for learning, prototyping, or testing IoT systems.

---

## Features

- Simulates multiple sensor devices 📡  
- Generates realistic temperature 🌡️ and humidity 💧 values  
- Sends data to InfluxDB 2.x time-series database  
- Visualize data live with Grafana dashboards 📊  
- Easy to configure and extend 🛠️  

---

## Technologies Used

- Python  
- `influxdb-client` Python package  
- InfluxDB 2.x (time-series database)  
- Grafana (visualization)  
- Docker (optional, for running InfluxDB and Grafana easily)  

---

## Installation & Setup

1. **Install Python 3.x** on your machine if not already installed.

2. Install the required Python package with:  
   ```bash
   pip install influxdb-client
