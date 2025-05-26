import random
import time
from influxdb_client import InfluxDBClient, Point, WritePrecision

# InfluxDB connection details
url = "http://localhost:8086"
token = "my-super-token"
org = "my-org"
bucket = "sensor_data_bucket"

# Initialize InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)

# List of sensor device names
devices = ["sensor1", "sensor2", "sensor3"]

# Simulate IoT sensor data
def simulate_sensor_data():
    temperature = round(random.uniform(15.0, 30.0), 2)
    humidity = round(random.uniform(40.0, 80.0), 2)
    return temperature, humidity

# Write data to InfluxDB
def write_to_influxdb(device, temperature, humidity):
    point = Point("sensor_data") \
        .tag("device", device) \
        .field("temperature", temperature) \
        .field("humidity", humidity) \
        .time(time.time_ns(), WritePrecision.NS)

    write_api = client.write_api()
    write_api.write(bucket=bucket, org=org, record=point)

# Main loop
try:
    while True:
        for device in devices:
            temp, hum = simulate_sensor_data()
            print(f"{device} → Temperature: {temp}°C, Humidity: {hum}%")
            write_to_influxdb(device, temp, hum)
        time.sleep(5)

except KeyboardInterrupt:
    print("Simulation stopped.")

finally:
    client.close()
