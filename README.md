# 🛡️ Secure MQTT Backend (Flask)

A robust Flask-based backend designed to simulate a **Secure MQTT Broker environment**. This project demonstrates **device authentication using certificates** and **end-to-end encrypted messaging** using symmetric key cryptography.

---

## 📖 Project Overview

This system provides a **RESTful API** to manage IoT device communication securely.

* Ensures messages sent over the "wire" are **encrypted**
* Simulates a **secure MQTT communication model**
* Allows only **authorized devices** to decrypt payloads

🔗 **Live Demo:** [http://secure-mqtt-backend-final.onrender.com](http://secure-mqtt-backend-final.onrender.com)

---

## 🧰 Tech Stack

* **Backend:** Python, Flask
* **Database:** SQLite
* **Encryption:** Cryptography (Fernet)
* **Server:** Gunicorn
* **Deployment:** Render

---

## 🛠️ Key Features

### 🔐 Certificate Generation

* Generates **32-byte Fernet keys** dynamically
* Assigns unique **device fingerprints**

### 📡 Secure Messaging

* Supports **plaintext (insecure)** and **encrypted (secure)** modes
* Simulates real-world IoT communication scenarios

### 🗂️ Message Logging

* Stores:

  * Timestamps
  * Topics
  * Encrypted "wire" payloads

### 🔍 Live Decryption Utility

* Decrypt messages server-side for verification
* Helps debug and validate encryption flow

### ☁️ Cloud Optimized

* Ready for deployment on **Render**
* Supports:

  * Dynamic port binding
  * SSL termination

---

## 🚀 Getting Started

### 1️⃣ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/secure-mqtt-backend.git
cd secure-mqtt-backend
pip install -r requirements.txt
```

---

### 2️⃣ Local Development

Run the Flask server locally:

```bash
python app.py
```

Server will run at:
👉 [http://localhost:5000](http://localhost:5000)

---

### 3️⃣ Production Deployment (Render)

Use the following configuration:

* **Build Command:**

```bash
pip install -r requirements.txt
```

* **Start Command:**

```bash
gunicorn app:app
```

---

## 📡 API Reference

### 🔐 Certificates

| Endpoint         | Method | Description                          |
| ---------------- | ------ | ------------------------------------ |
| `/generate_cert` | POST   | Create a new device key/fingerprint  |
| `/certs`         | GET    | Retrieve all registered certificates |

---

### 📩 Messaging

| Endpoint    | Method | Description                                    |
| ----------- | ------ | ---------------------------------------------- |
| `/send`     | POST   | Send a message (topic, payload, mode required) |
| `/messages` | GET    | Retrieve message history (supports `limit`)    |
| `/decrypt`  | POST   | Decrypt payload using certificate              |

---

## 🔐 Security Implementation

This project uses **Fernet symmetric encryption**, which provides both confidentiality and integrity.

* **Encryption Algorithm:** AES-128 (CBC mode)
* **Padding:** PKCS7
* **Authentication:** HMAC with SHA-256

✔ Ensures:

* Data confidentiality
* Message integrity
* Protection against tampering

---

## 📂 Project Structure

```
secure-mqtt-backend/
│
├── app.py              # Main Flask application
├── data.db             # SQLite database (auto-generated)
├── requirements.txt    # Dependencies
├── certs/              # Optional SSL certificates
└── README.md           # Documentation
```

---

## 🌟 Highlights

* Combines **IoT + Security + Backend Engineering**
* Demonstrates **real-world encryption workflows**
* Ideal for:

  * Academic projects
  * Portfolio showcasing
  * Learning secure system design

---

## 📌 Future Improvements

* Add MQTT broker integration (Mosquitto)
* Implement device-level access control (ACL)
* Add JWT-based API authentication
* Build frontend dashboard for visualization

---

## 👨‍💻 Author

**Abhay Kumar**

---

## 📜 License

This project is open-source and available under the MIT License.
