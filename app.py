import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="داشبورد @mj3150s20", layout="centered")
st.title("🚀 داشبورد موبایل")
st.caption(f"ساخته‌شده در: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

API_KEY = st.secrets.get("XAI_API_KEY")
if not API_KEY:
    st.error("کلید API پیدا نشد!")
    st.stop()

MODEL = "grok-4"

@st.cache_data(ttl=3600)
def get_challenge():
    prompt = f"یه چالش فنی فارسی برای @mj3150s20 بنویس. تاریخ: {datetime.now().strftime('%Y-%m-%d')}"
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        payload = {"model": MODEL, "messages": [{"role": "user", "content": prompt}], "temperature": 0.9}
        r = requests.post("https://api.x.ai/v1/chat/completions", json=payload, headers=headers)
        return r.json()["choices"][0]["message"]["content"]
    except:
        return "خطا در اتصال به API"

if st.button("چالش جدید"):
    with st.spinner("در حال دریافت..."):
        st.markdown(get_challenge())
else:
    st.info("دکمه بالا رو بزن!")

st.markdown("---")
st.markdown("ساخته‌شده توسط @mj3150s20 با گوشی 📱")
