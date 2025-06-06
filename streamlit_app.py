import os
import random
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# ─── Load your API key ──────────────────────────────────────────────────────────
load_dotenv()  # loads .env in local dev

# When deployed, Streamlit will merge your UI‐Secrets into os.environ
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("🚨 GEMINI_API_KEY not set! Check your .env or Streamlit secrets.")
    st.stop()

client = genai.Client(api_key=API_KEY)

# ─── Your 52 cards dict ─────────────────────────────────────────────────────────
cards = {
  "1":  {"title": "First Step", "content": "Every journey begins..."},
  # … all 52 …
  "52": {"title": "Disruptive Innovation Business", "content": "Disruption can pave the way..."}
}

# ─── Streamlit UI ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="🎴 KoolBox", layout="centered")
st.title("🎴 KoolBox")

# Draw or reuse card
if "card_key" not in st.session_state or st.button("Draw New Card"):
    st.session_state.card_key = random.choice(list(cards.keys()))
    st.session_state.answer = None

card = cards[st.session_state.card_key]
st.subheader(card["title"])
st.write(card["content"])

# Ask a question
question = st.text_area("Ask KoolBox…", height=80)
if st.button("Get Answer") and question.strip():
    prompt = (
        f"{card['title']}\n{card['content']}\n\n"
        "You will describe what the card is about and answer the question "
        "based on this and come up with a positive answer. "
        "Keep it concise and strip all markup styling.\n\n"
        f"Question: {question}"
    )
    res = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(system_instruction=prompt),
        contents=question
    )
    st.session_state.answer = res.text

# Show answer
if st.session_state.get("answer"):
    st.markdown("### 💡 Answer")
    st.write(st.session_state.answer)
