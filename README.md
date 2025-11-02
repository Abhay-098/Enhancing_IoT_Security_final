# Full-stack Server-Client Secure vs Insecure Demo (Fixed)

This version removes deprecated imports and is ready for deployment on Render + Streamlit Cloud.

## Contents
- backend/server.py  → Flask REST API with SQLite persistence (runs with TLS if certs exist)
- frontend/streamlit_app.py → Streamlit UI that talks to backend
- scripts/generate_server_cert.sh → generate self-signed TLS certs
- requirements.txt → dependencies

### Run locally
```bash
pip install -r requirements.txt
python backend/server.py
streamlit run frontend/streamlit_app.py
```

### Deploy to Render
Root Directory: backend  
Build Command: pip install -r requirements.txt  
Start Command: python server.py
