import streamlit as st
import pandas as pd

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Data Science Personality Quiz", layout="centered")

# ---------- TITLE ----------
st.title("🧬 What's Your Data Science Personality?")
st.write("Take this fun quiz to discover your **data superpower!** 💡")

# ---------- SCORE TRACKER ----------
scores = {
    "viz": 0,
    "ml": 0,
    "cleaning": 0,
    "insight": 0,
    "dashboard": 0
}

# ---------- QUESTIONS ----------
questions = [
    ("🎯 What do you enjoy most in a data project?", [
        "Finding hidden patterns",
        "Cleaning messy data",
        "Making beautiful charts",
        "Building smart models",
        "Creating dashboards for decisions"
    ]),
    ("🛠️ What's your favorite data tool?", [
        "Power BI or Looker",
        "Pandas or OpenRefine",
        "SQL or NLP libraries",
        "Scikit-learn or XGBoost",
        "Plotly or Tableau"
    ]),
    ("🐾 Your data spirit animal?", [
        "Ant (organized, reliable)",
        "Peacock (stylish, colorful)",
        "Wolf (strategic, sharp)",
        "Owl (observant, curious)",
        "Beaver (builder, fixer)"
    ]),
    ("📂 You open a messy CSV file. You:", [
        "Study the weird patterns",
        "Fix every row",
        "Document issues for reporting",
        "Start plotting it",
        "Train a model on it anyway"
    ]),
    ("💬 What do people say you're good at?", [
        "Explaining clearly with visuals",
        "Fixing broken stuff",
        "Solving complex problems",
        "Making things look amazing",
        "Seeing what others miss"
    ]),
    ("🎮 Which task sounds the most fun?", [
        "Designing colorful dashboards",
        "Writing SQL queries to explore data",
        "Building machine learning pipelines",
        "Cleaning columns and formatting",
        "Visual storytelling with data"
    ]),
    ("🧰 What’s your secret weapon?", [
        "Clear communication",
        "Model accuracy",
        "Pattern recognition",
        "Chart design",
        "Data wrangling"
    ]),
    ("👥 Your ideal team role is:", [
        "Insight digger",
        "Dashboard designer",
        "ML engineer",
        "Visualization expert",
        "Data janitor"
    ]),
    ("🔥 What motivates you most?", [
        "Spotting hidden stories",
        "Building smart tools",
        "Fixing messy problems",
        "Helping teams see clearly",
        "Making complex things look simple"
    ]),
    ("🎁 Choose a gift for your data friend:", [
        "Color palettes and fonts",
        "Deep learning course",
        "SQL cookbook",
        "Dashboard templates",
        "Data cleaning scripts"
    ])
]

# ---------- KEYWORDS TO MATCH ----------
personality_keywords = {
    "viz": ["chart", "plot", "visual", "peacock", "amazing", "design", "storytelling", "fonts", "color"],
    "ml": ["model", "ai", "xgboost", "neural", "wolf", "train", "ml", "deep", "engineer", "pipelines", "accuracy"],
    "cleaning": ["clean", "fix", "pandas", "beaver", "wrangling", "format", "janitor", "scripts"],
    "insight": ["pattern", "trend", "sql", "owl", "see", "study", "stories", "recognition", "digger", "cookbook"],
    "dashboard": ["dashboard", "report", "power bi", "look", "ant", "explain", "designer", "templates"]
}

# ---------- COLLECT ANSWERS ----------
answers = []
for i, (question, options) in enumerate(questions):
    selected = st.radio(f"{i+1}. {question}", [""] + options, key=f"q{i+1}")
    answers.append(selected)

# ---------- REVEAL RESULT ----------
if st.button("🎯 REVEAL MY DATA PERSONALITY!"):
    for answer in answers:
        answer_lower = answer.lower()
        for personality, keywords in personality_keywords.items():
            if any(keyword in answer_lower for keyword in keywords):
                scores[personality] += 1

    top = max(scores, key=scores.get)

    personalities = {
        "viz": {
            "emoji": "🎨",
            "title": "The Data Viz Artist",
            "desc": "You make data beautiful and clear. People feel your charts."
        },
        "ml": {
            "emoji": "🤖",
            "title": "The ML Mastermind",
            "desc": "You love solving problems and training smart systems."
        },
        "cleaning": {
            "emoji": "🧼",
            "title": "The Data Cleaning Wizard",
            "desc": "You're the hero who turns chaos into clean, usable data."
        },
        "insight": {
            "emoji": "🔍",
            "title": "The Insight Hunter",
            "desc": "You live for discovering hidden stories others miss."
        },
        "dashboard": {
            "emoji": "📊",
            "title": "The Dashboard Boss",
            "desc": "You transform complex data into clear, actionable dashboards."
        }
    }

    # 🎉 Celebration
    st.balloons()

    # 🎯 Result card
    p = personalities[top]
    st.markdown(f"""
    <div style="border: 2px solid #bbb; border-radius: 12px; padding: 1.2em; background-color: #f9f9f9;">
        <h2 style="color:#333;">{p['emoji']} <strong>{p['title']}</strong></h2>
        <p style="font-size: 1.1em;">{p['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.toast("🥳 Personality revealed! Scroll up to view your result.")

    # 📊 Score Breakdown Chart
    st.markdown("### 📊 Your Full Score Breakdown")
    personality_labels = {
        "viz": "🎨 Data Viz Artist",
        "ml": "🤖 ML Mastermind",
        "cleaning": "🧼 Cleaning Wizard",
        "insight": "🔍 Insight Hunter",
        "dashboard": "📊 Dashboard Boss"
    }

    score_df = pd.DataFrame({
        "Personality": [personality_labels[key] for key in scores],
        "Score": [scores[key] for key in scores]
    }).sort_values(by="Score", ascending=True)

    st.bar_chart(score_df.set_index("Personality"))
