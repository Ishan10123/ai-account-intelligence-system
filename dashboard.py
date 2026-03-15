import streamlit as st
import json
import os
import subprocess
import pandas as pd
import time
import random

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Account Intelligence Platform",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Account Intelligence Platform")
st.markdown("Convert anonymous visitor signals into **actionable sales intelligence**.")

# ---------------------------------------------------
# RUN PIPELINE BUTTON
# ---------------------------------------------------

if st.button("🚀 Run AI Analysis Pipeline"):
    subprocess.run(["python", "-m", "pipeline.intelligence_pipeline"])
    st.success("Pipeline executed successfully")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

FILE_PATH = "account_intelligence_output.json"

if not os.path.exists(FILE_PATH):
    st.error("No intelligence data found. Run the pipeline first.")
    st.stop()

with open(FILE_PATH) as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ---------------------------------------------------
# INTELLIGENCE SCORE CALCULATION
# ---------------------------------------------------

def compute_score(row):

    score = 0
    score += row["intent_score"] * 10
    score += len(row["business_signals"]) * 5

    if row["intent_stage"] == "Evaluation":
        score += 30

    if row["persona"] in ["Sales Leader", "Technical Buyer"]:
        score += 10

    return score

df["intelligence_score"] = df.apply(compute_score, axis=1)

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.header("🔎 Filters")

stage_filter = st.sidebar.selectbox(
    "Intent Stage",
    ["All","Research","Consideration","Evaluation"]
)

persona_filter = st.sidebar.selectbox(
    "Persona",
    ["All"] + sorted(df["persona"].unique().tolist())
)

search_company = st.sidebar.text_input("Search Company")

filtered_df = df.copy()

if stage_filter != "All":
    filtered_df = filtered_df[filtered_df["intent_stage"] == stage_filter]

if persona_filter != "All":
    filtered_df = filtered_df[filtered_df["persona"] == persona_filter]

if search_company:
    filtered_df = filtered_df[
        filtered_df["company"].str.contains(search_company, case=False)
    ]

# ---------------------------------------------------
# KPI DASHBOARD
# ---------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Accounts Analyzed", len(df))
col2.metric("Filtered Accounts", len(filtered_df))
col3.metric("Evaluation Stage", len(df[df["intent_stage"]=="Evaluation"]))
col4.metric("Avg Intent Score", round(df["intent_score"].mean(),2))

st.divider()

# ---------------------------------------------------
# INTENT DISTRIBUTION
# ---------------------------------------------------

st.subheader("📊 Intent Distribution")

intent_counts = df["intent_stage"].value_counts()

st.bar_chart(intent_counts)

st.divider()

# ---------------------------------------------------
# LEADERBOARD
# ---------------------------------------------------

st.subheader("🏆 Top High-Intent Accounts")

leaderboard = df.sort_values(
    by="intelligence_score",
    ascending=False
).head(10)

st.dataframe(
    leaderboard[["company","intent_stage","intent_score","intelligence_score"]],
    use_container_width=True
)

st.divider()

# ---------------------------------------------------
# ACCOUNT INTELLIGENCE CARDS
# ---------------------------------------------------

st.subheader("🧠 Account Intelligence")

for _, record in filtered_df.iterrows():

    with st.expander(f"{record['company']} | Intelligence Score: {record['intelligence_score']}"):

        col1, col2 = st.columns(2)

        # ---------------------------------------------------
        # COMPANY PROFILE
        # ---------------------------------------------------

        with col1:

            st.markdown("### Company Profile")

            st.write("Industry:", record["industry"])
            st.write("Domain:", record["domain"])
            st.write("Company Size:", record["company_size"])
            st.write("Headquarters:", record["headquarters"])

            if record.get("founding_year"):
                st.write("Founded:", record["founding_year"])

            if record.get("business_description"):
                st.write("Description:", record["business_description"])

        # ---------------------------------------------------
        # BUYER INTELLIGENCE
        # ---------------------------------------------------

        with col2:

            st.markdown("### Buyer Intelligence")

            st.write("Persona:", record["persona"])

            if record.get("persona_confidence"):
                st.write("Persona Confidence:", f"{record['persona_confidence']}%")

            st.write("Intent Score:", record["intent_score"])

            st.progress(record["intent_score"] / 10)

            st.write("Intent Stage:", record["intent_stage"])

            if record.get("company_match_confidence"):
                st.write("Company Match Confidence:", f"{record['company_match_confidence']}%")

        # ---------------------------------------------------
        # TECHNOLOGY STACK
        # ---------------------------------------------------

        st.markdown("### Technology Stack")

        tech = record["technology_stack"]

        tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)

        tech_col1.metric("CRM", tech["CRM"])
        tech_col2.metric("Marketing", tech["Marketing"])
        tech_col3.metric("Website", tech["Website"])
        tech_col4.metric("Analytics", tech["Analytics"])

        # ---------------------------------------------------
        # LEADERSHIP
        # ---------------------------------------------------

        if record.get("leadership"):

            st.markdown("### Leadership Team")

            for role, name in record["leadership"].items():
                st.write(f"{role}: {name}")

        # ---------------------------------------------------
        # VISITOR BEHAVIOR SIGNALS
        # ---------------------------------------------------

        if record.get("behavior_signals"):

            st.markdown("### Key Visitor Signals Observed")

            for page in record["behavior_signals"]:
                st.write("•", page)

        # ---------------------------------------------------
        # BUSINESS SIGNALS
        # ---------------------------------------------------

        st.markdown("### Business Signals")

        for signal in record["business_signals"]:
            st.info(signal)

        # ---------------------------------------------------
        # AI SUMMARY
        # ---------------------------------------------------

        st.markdown("### AI Intelligence Summary")

        st.success(record["ai_summary"])

        # ---------------------------------------------------
        # SALES ACTIONS
        # ---------------------------------------------------

        st.markdown("### Recommended Sales Actions")

        for action in record["recommended_sales_actions"]:
            st.write("✔", action)

st.divider()

# ---------------------------------------------------
# REAL-TIME VISITOR SIMULATION
# ---------------------------------------------------

st.subheader("⚡ Real-Time Visitor Simulation")

if st.button("Start Visitor Simulation"):

    simulation_container = st.container()

    for i in range(10):

        sample = df.sample(1).iloc[0]

        with simulation_container:

            st.warning("🚨 New Visitor Detected")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"Company: {sample['company']}")
                st.write(f"Persona: {sample['persona']}")

            with col2:
                st.write(f"Intent Stage: {sample['intent_stage']}")
                st.write(f"Intent Score: {sample['intent_score']}")

            st.progress(sample["intent_score"] / 10)

            st.divider()

        time.sleep(random.uniform(1.5, 3))