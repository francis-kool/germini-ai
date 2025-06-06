# KoolBox Streamlit App

## Setup (local)

1. `git clone ...`
2. `cd koolbox-streamlit`
3. `python3 -m venv venv && source venv/bin/activate`
4. `pip install -r requirements.txt`
5. Copy `.env.example` ➔ `.env` and fill in your `GEMINI_API_KEY`
6. `streamlit run streamlit_app.py`

## Deploy on Streamlit Cloud

1. Push your repo (without the real `.env` or `secrets.toml`) to GitHub.
2. Go to Streamlit Cloud → New app → connect your repo.
3. In **Settings → Secrets**, add  
   `GEMINI_API_KEY = your_real_api_key_here`
4. Deploy!
