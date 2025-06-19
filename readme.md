# Medical Assistant AI
### Personalized AI agent to locate nearby clinic and hospitals to based on user inputs

#### Mobile Device Integration for Location Access

To enable location-based features using your mobile device's GPS, please follow the steps below:

* Enable Mobile Data on your smartphone.

* Turn on Mobile Hotspot on the same device.

* Connect your laptop to the mobile hotspot network.

This setup allows the application to access the device’s GPS data through the internet connection provided by your mobile phone.


### 📦 Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/medical-assistant-ai.git
cd medical-assistant-ai
```

#### 2. Set Up a Virtual Environment
```bash
python3 -m venv medical-assistant-ai-env
source medical-assistant-ai-env/bin/activate
```
🪟 On Windows, use:
```bash
medical-assistant-ai-env\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
#### 4. SSL Certificate Setup
```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```


## 🚀 Running the Server
```bash
python3 src/server.py
```