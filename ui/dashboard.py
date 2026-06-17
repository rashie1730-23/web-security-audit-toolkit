import streamlit as st
import pandas as pd
import plotly.express as px

from database.history_service import get_audits

def dashboard_page():

    if not st.session_state["user"]:

        st.warning(
            "Please login first"
        )

        st.stop()

    st.markdown("""
<div style="
padding:25px;
border-radius:20px;
background:linear-gradient(
90deg,
#2563eb,
#7c3aed
);
margin-bottom:20px;
">

<h1 style="color:white;">
🛡️ Security Operations Center
</h1>

<p style="color:white;">
Monitor website security posture,
track vulnerabilities and manage audits.
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown(f"### Welcome back, {st.session_state['user']['name']} 👋")

    audits = get_audits(st.session_state["user"]["email"])

    total_audits = len(audits)

    if total_audits > 0:

        avg_risk = round(
            sum(
                audit.risk_score
                for audit in audits
            ) / total_audits,
            2
        )

        high_risk = len([
            audit
            for audit in audits
            if audit.risk_score >= 70
        ])

    else:

        avg_risk = 0
        high_risk = 0

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Audits",
        total_audits
    )

    col2.metric(
        "Average Risk Score",
        avg_risk
    )

    col3.metric(
        "High Risk Sites",
        high_risk
    )

    st.header("📜 Recent Activity")

    if audits:
        chart_data = []

        for audit in audits:
            chart_data.append({
                "Date": audit.created_at,
                "Risk Score": audit.risk_score
            })

        df_chart = pd.DataFrame(chart_data)

        fig = px.line(
            df_chart,
            x="Date",
            y="Risk Score",
            markers=True,
            title="Risk Score Trend"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )
    if audits:
        high = 0
        medium = 0
        low = 0

        for audit in audits:
            if audit.risk_score >= 70:
                high += 1
            elif audit.risk_score >= 40:
                medium += 1
            else:
                low += 1

        pie_data = pd.DataFrame({
            "Category": [
                "High",
                "Medium",
                "Low"
            ],
            "Count": [
                high,
                medium,
                low
            ]
        })

        pie = px.pie(
            pie_data,
            names="Category",
            values="Count",
            title="Audit Severity Distribution"
        )

        st.plotly_chart(
            pie,
            width="stretch"
        )