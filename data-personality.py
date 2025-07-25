import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title=" Data Science Personality Quiz", layout="centered")

# ---------- TITLE ----------
st.title("🧬 What's Your Data Science Personality?")
st.write("Answer 5 quick questions to discover your data superpower!")

# --------------Score tracker---------------

scores = {
    "viz": 0,        # 🎨 Data Viz Artist
    "ml": 0,         # 🤖 ML Mastermind
    "cleaning": 0,   # 🧼 Data Cleaning Wizard
    "insight": 0,    # 🔍 Insight Hunter
    "dashboard": 0   # 📊 Dashboard Boss
}

# ----------------------ask question-----------------

q1=st.radio("1. What do you enjoy most in a data project?",[
    "Making beautiful charts",         # viz
    "Building smart models",           # ml
    "Cleaning messy data",             # cleaning
    "Finding hidden patterns",         # insight
    "Creating dashboards for decisions" # dashboard
])

q2 = st.radio("2. What's your favorite data tool?", [
    "Plotly or Tableau",           # viz
    "Scikit-learn or XGBoost",     # ml
    "Pandas or OpenRefine",        # cleaning
    "SQL or NLP libraries",        # insight
    "Power BI or Looker"           # dashboard
])

q3 = st.radio("3. Your data spirit animal?", [
    "🦚 Peacock (stylish, colorful)",  # viz
    "🐺 Wolf (strategic, sharp)",      # ml
    "🦫 Beaver (builder, fixer)",      # cleaning
    "🦉 Owl (observant, curious)",     # insight
    "🐜 Ant (organized, reliable)"     # dashboard
])

q4 = st.radio("4. You open a messy CSV file. You:", [
    "Start plotting it",           # viz
    "Train a model on it anyway",  # ml
    "Fix every row",               # cleaning
    "Study the weird patterns",    # insight
    "Document issues for reporting" # dashboard
])

q5 = st.radio("5. What do people say you're good at?", [
    "Making things look amazing",      # viz
    "Solving complex problems",        # ml
    "Fixing broken stuff",             # cleaning
    "Seeing what others miss",         # insight
    "Explaining clearly with visuals"  # dashboard
])

# --------------------keywords to match---------------

personality_keywords = {
    "viz": ["chart", "plot", "visual", "tableau", "peacock", "look", "amazing"],
    "ml": ["model", "ai", "xgboost", "neural", "wolf", "train", "problem"],
    "cleaning": ["clean", "mess", "pandas", "beaver", "fix"],
    "insight": ["pattern", "trend", "sql", "owl", "see", "study"],
    "dashboard": ["dashboard", "report", "power bi", "look", "ant", "explain"]
}

# -----------------score calculation---------------

answers = [q1,q2,q3,q4,q5]

for answer in answers:
    answer_lower= answer.lower()
    for personality, keywords in enumerate(personality_keywords):
        if any(keyword in answer_lower for keyword in keywords):
            scores[personality]+=1
            
# -------------personality reveal----------------------------
if st.button("🔍 Reveal My Personality!"):
    top = max(scores, key= scores.get)

    st.subheader("🎯 Your Data Personality:")

    if top == "viz":
        st.success("🎨 **The Data Viz Artist**\n\nYou make data beautiful and clear. People feel your charts.")
    elif top == "ml":
        st.success("🤖 **The ML Mastermind**\n\nYou love solving problems and training smart systems.")
    elif top == "cleaning":
        st.success("🧼 **The Data Cleaning Wizard**\n\nYou're the hero who turns chaos into clean data.")
    elif top == "insight":
        st.success("🔍 **The Insight Hunter**\n\nYou live for those hidden discoveries in data.")
    elif top == "dashboard":
        st.success("📊 **The Dashboard Boss**\n\nYou translate data into decisions with clarity.")


st.toast("✅ Quiz complete! Scroll to see your result.")