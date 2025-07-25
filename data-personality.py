import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Data Science Personality Quiz", layout="centered")

st.title("🧬 What's Your Data Science Personality?")
st.write("Answer these fun questions to discover your **data superpower**!")

# ---------- Score Tracker ----------
scores = {
    "viz": 0,        # 🎨 Data Viz Artist
    "ml": 0,         # 🤖 ML Mastermind
    "cleaning": 0,   # 🧼 Data Cleaning Wizard
    "insight": 0,    # 🔍 Insight Hunter
    "dashboard": 0   # 📊 Dashboard Boss
}

# ---------- Personality Keywords ----------
personality_keywords = {
    "viz": ["chart", "plot", "visual", "tableau", "look", "amazing"],
    "ml": ["model", "ai", "xgboost", "neural", "train", "problem"],
    "cleaning": ["clean", "mess", "pandas", "fix", "broken"],
    "insight": ["pattern", "trend", "sql", "study", "see"],
    "dashboard": ["dashboard", "report", "power bi", "explain"]
}

# ---------- Questions ----------
questions = [
    ("1. What do you enjoy most in a data project?", [
        "Finding hidden patterns",         # insight
        "Cleaning messy data",             # cleaning
        "Making beautiful charts",         # viz
        "Creating dashboards for decisions",  # dashboard
        "Building smart models"            # ml
    ]),
    ("2. What's your favorite data tool?", [
        "Power BI or Looker",              # dashboard
        "Scikit-learn or XGBoost",         # ml
        "Plotly or Tableau",               # viz
        "SQL or NLP libraries",            # insight
        "Pandas or OpenRefine"             # cleaning
    ]),
    ("3. Your data spirit animal?", [
        "Beaver (builder, fixer)",         # cleaning
        "Owl (observant, curious)",        # insight
        "Wolf (strategic, sharp)",         # ml
        "Peacock (stylish, colorful)",     # viz
        "Ant (organized, reliable)"        # dashboard
    ]),
    ("4. You open a messy CSV file. You:", [
        "Start plotting it",               # viz
        "Fix every row",                   # cleaning
        "Document issues for reporting",   # dashboard
        "Study the weird patterns",        # insight
        "Train a model on it anyway"       # ml
    ]),
    ("5. What do people say you're good at?", [
        "Fixing broken stuff",             # cleaning
        "Making things look amazing",      # viz
        "Explaining clearly with visuals", # dashboard
        "Seeing what others miss",         # insight
        "Solving complex problems"         # ml
    ]),
    ("6. If data were food, you'd be the:", [
        "Recipe creator (modeling expert)",     # ml
        "Chef (beautiful plating)",             # viz
        "Inspector (quality controller)",       # cleaning
        "Nutritionist (insights extractor)",    # insight
        "Waiter (delivering with clarity)"      # dashboard
    ]),
    ("7. Your dream project involves:", [
        "Predicting the future with data",      # ml
        "Designing impactful dashboards",       # dashboard
        "Untangling complex raw data",          # cleaning
        "Visual storytelling",                  # viz
        "Finding trends no one noticed"         # insight
    ]),
    ("8. A colleague asks for help with messy data. You:", [
        "Jump in and clean it up",              # cleaning
        "Plot the distributions",               # viz
        "Document the issues clearly",          # dashboard
        "Look for odd trends",                  # insight
        "Try training a quick model"            # ml
    ]),
    ("9. Which sounds most like you?", [
        "Pattern detector",                     # insight
        "Visualizer",                           # viz
        "Fixer",                                # cleaning
        "Strategist",                           # ml
        "Communicator"                          # dashboard
    ]),
    ("10. Which role would you thrive in?", [
        "Data storyteller",                     # viz
        "Machine learning engineer",            # ml
        "Data janitor",                         # cleaning
        "Insight analyst",                      # insight
        "Business intelligence developer"       # dashboard
    ])
]

# ---------- Capture Answers ----------
answers = []

for q_text, q_options in questions:
    response = st.radio(q_text, q_options, index=None)
    answers.append(response)

# ---------- Score Calculation ----------
if st.button("🎯 REVEAL MY DATA PERSONALITY!"):
    for answer in answers:
        if answer:  # Ensure user selected something
            answer_lower = answer.lower()
            for personality, keywords in personality_keywords.items():
                if any(keyword in answer_lower for keyword in keywords):
                    scores[personality] += 1

    top = max(scores, key=scores.get)

    # 🎉 Celebration
    st.balloons()

    # ---------- Result ----------
    st.markdown(f"### {top.title()} Personality")
    if top == "viz":
        st.info("🎨 **The Data Viz Artist** — You make data beautiful and clear. People feel your charts.")
    elif top == "ml":
        st.info("🤖 **The ML Mastermind** — You love solving problems and training smart systems.")
    elif top == "cleaning":
        st.info("🧼 **The Data Cleaning Wizard** — You're the hero who turns chaos into clean data.")
    elif top == "insight":
        st.info("🔍 **The Insight Hunter** — You live for those hidden discoveries in data.")
    elif top == "dashboard":
        st.info("📊 **The Dashboard Boss** — You translate data into decisions with clarity.")

    # ---------- Bar Chart ----------
    st.markdown("### 📊 Your Full Score Breakdown")

    # Rename for display
    labels = {
        "viz": "🎨 Data Viz Artist",
        "ml": "🤖 ML Mastermind",
        "cleaning": "🧼 Cleaning Wizard",
        "insight": "🔍 Insight Hunter",
        "dashboard": "📊 Dashboard Boss"
    }

    df = pd.DataFrame({
        "Personality": [labels[k] for k in scores.keys()],
        "Score": list(scores.values())
    })

    fig = px.bar(
        df,
        x="Personality",
        y="Score",
        color="Personality",
        text="Score",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    fig.update_layout(xaxis_tickangle=0, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
