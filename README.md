# IoT Telemetry Simulation with Python and ThingsBoard

[Español](./README_es.md)

This repository contains a simple IoT telemetry simulation written in Python.  
It emulates a temperature sensor by generating random values and sending them periodically to the ThingsBoard Cloud platform using its REST API.

The project is intended for learning and practice purposes, demonstrating the basic flow of IoT data:

Device → Internet → IoT Platform (ThingsBoard)

---

## Project Overview

The main script (`telemetria.py`) simulates a temperature sensor:

- Generates random temperature values between 18°C and 32°C.
- Sends telemetry data to ThingsBoard every 5 seconds.
- Authenticates using a device access token.
- Uses HTTP POST requests to publish data.

Although this project uses a Python script instead of a physical sensor, it represents the same logical behavior as a real IoT device.

---

## Repository Structure

```
.
├── telemetria.py          # Main telemetry script
├── requirements.txt      # Python dependencies
├── token.txt.example     # Example file for the ThingsBoard device token
├── token.txt             # Your real token (ignored by git)
├── .gitignore
├── LICENSE
├── README.md
└── README_es.md
```

---

## Requirements

- Python 3.x
- Internet connection
- A ThingsBoard Cloud account (demo or self-hosted)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

1. Create a device in ThingsBoard (for example in https://demo.thingsboard.io).
2. Copy the device access token.
3. Create a file called `token.txt` in the project root.
4. Paste your token inside `token.txt`.

You can use `token.txt.example` as a reference.

Important:  
`token.txt` is ignored by Git to avoid exposing credentials.

---

## Running the Script

Execute:

```bash
python telemetria.py
```

The script will:

- Generate a random temperature value.
- Send it to ThingsBoard.
- Repeat every 5 seconds.

You should see the telemetry data appear in your ThingsBoard dashboard.

Stop the script with `Ctrl + C`.

---

## Notes

- The 5-second interval is only for testing purposes. In real IoT deployments, telemetry is usually sent every few minutes to reduce network usage and power consumption.
- In production environments, MQTT is commonly used instead of HTTP for efficiency.

---

## License

This project is licensed under the Apache License 2.0.  
See the `LICENSE` file for details.

---

## Educational Purpose

This repository is part of an academic IoT practice and is intended to demonstrate:

- Basic device telemetry
- REST API communication
- Token-based authentication
- Integration with an IoT platform

## Team

This project was developed by:

- **Daniel Carrasco**  
  [GitHub](https://github.com/CarrasDev) | [LinkedIn](https://www.linkedin.com/in/danielcarrascoluque/)

- **Vanesa Sierra**  
  [GitHub](https://github.com/SierraTrace) | [LinkedIn](https://www.linkedin.com/in/vanesasierra/)

- **Raul Estevez**  
  [GitHub](https://github.com/RaulEstevezA) | [LinkedIn](https://www.linkedin.com/in/raulesteveza/)

