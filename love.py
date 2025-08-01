import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import random
import time


# ------------------- SETUP -------------------
# Replace with your actual start date
start_date = datetime(2025, 2, 15, 17, 50)  # <--- CHANGE THIS

# Current time
now = datetime.now()

# Time difference
rd = relativedelta(now, start_date)
delta = now - start_date

# Countdown to next anniversary
this_year_anniv = datetime(now.year, start_date.month, start_date.day, start_date.hour, start_date.minute)
if this_year_anniv < now:
    next_anniv = this_year_anniv.replace(year=now.year + 1)
else:
    next_anniv = this_year_anniv
countdown = next_anniv - now

# Love quotes
love_quotes = [
    "I still get butterflies even though I've seen you a hundred times.",
    "Every love story is beautiful, but ours is my favorite.",
    "You’re my today and all of my tomorrows.",
    "My favorite place is inside your hug.",
    "Forever is a long time, but I wouldn’t mind spending it by your side.",
    "In your smile, I see something more beautiful than stars.",
    "With you, every moment is love in its purest form."
]

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="Our Love Journey",
    page_icon="💖",
    layout="centered",
)

# ------------------- CUSTOM STYLES -------------------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Dancing+Script&display=swap');

        html, body, [class*="css"] {
            font-family: 'Dancing Script', cursive;
            background: linear-gradient(135deg, #fff0f5, #ffd6e8);
            color: #4B004B;
        }
        .big-title {
            font-size: 48px;
            text-align: center;
            font-family: 'Pacifico', cursive;
            color: #b30059;
            margin-bottom: 10px;
        }
        .sub-text {
            font-size: 20px;
            text-align: center;
            color: #800040;
            margin-bottom: 40px;
        }
        .card {
            background-color: #fff8fc;
            border-radius: 20px;
            padding: 20px;
            margin: 10px;
            box-shadow: 2px 2px 10px #e6b8d1;
            text-align: center;
        }
        .time-value {
            font-size: 36px;
            font-weight: bold;
            color: #6a004c;
        }
        .time-label {
            font-size: 18px;
            color: #99004d;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #bb3e78;
            margin-top: 50px;
        }
        body::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: 0;
        pointer-events: none;
        background: url('https://i.imgur.com/3R5B6je.png') repeat;
        opacity: 0.05;
        animation: floatHearts 60s linear infinite;
    }

    @keyframes floatHearts {
        0% { background-position: 0 0; }
        100% { background-position: 0 -1000px; }
    }

    .main, .block-container {
        position: relative;
        z-index: 1;
    }

        
    </style>
""", unsafe_allow_html=True)

# ------------------- HEADER -------------------
st.markdown('<div class="big-title">💖 Our Love Journey 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">🕊️ Every second with you is a heartbeat of my happiest life 🕊️</div>', unsafe_allow_html=True)

# ------------------- TIME DISPLAY -------------------
st.markdown("### 🌹 Time Since We Started Dating")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="card"><div class="time-value">{rd.years}</div><div class="time-label">Years</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="card"><div class="time-value">{rd.months}</div><div class="time-label">Months</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="card"><div class="time-value">{rd.days}</div><div class="time-label">Days</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="card"><div class="time-value">{delta.seconds//3600}</div><div class="time-label">Hours Today</div></div>', unsafe_allow_html=True)

st.markdown("### 💘 Total Time Together")
st.markdown(f'<div class="card"><div class="time-value">{delta.days}</div><div class="time-label">Total Days</div></div>', unsafe_allow_html=True)
st.markdown(f'<div class="card"><div class="time-value">{delta.days//7}</div><div class="time-label">Total Weeks</div></div>', unsafe_allow_html=True)
st.markdown(f'<div class="card"><div class="time-value">{(rd.years * 12 + rd.months)}</div><div class="time-label">Total Months</div></div>', unsafe_allow_html=True)
st.markdown(f'<div class="card"><div class="time-value">{int(delta.total_seconds() // 3600)}</div><div class="time-label">Total Hours</div></div>', unsafe_allow_html=True)

# ------------------- COUNTDOWN -------------------
st.markdown("### 🎉 Countdown to Our Next Anniversary")
days, seconds = countdown.days, countdown.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
st.markdown(f'<div class="card"><div class="time-value">{days} days, {hours} hours, {minutes} minutes</div><div class="time-label">Left Until Our Anniversary</div></div>', unsafe_allow_html=True)

# ------------------- LOVE QUOTE -------------------
st.markdown("### 💌 Tap for a Random Love Note")
if st.button("💖 Show me some love!"):
    st.success(random.choice(love_quotes))

# ------------------- FOOTER -------------------
st.markdown('<div class="footer">Made with ❤️ by You, for the love of your life.</div>', unsafe_allow_html=True)
