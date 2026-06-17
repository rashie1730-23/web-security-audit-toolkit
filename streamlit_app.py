from database.history_service import (
    save_audit,
    get_audits
)
from ui.dashboard import dashboard_page
import streamlit as st
import pandas as pd

from modules.recon import get_website_info
from modules.ssl_check import get_ssl_info
from modules.headers_check import check_security_headers
from modules.risk_analyzer import analyze_headers
from modules.report_generator import generate_report
from modules.risk_score import calculate_risk_score
from modules.severity_stats import count_severities
from modules.crawler import crawl_internal_links
from modules.pdf_report import generate_pdf_report

from steganography.steg_ui import render_steganography
from modules.page_audit import audit_multiple_pages
from ui.register import register_page
from ui.login import login_page

if "user" not in st.session_state:

    st.session_state["user"] = None

# --------------------------------
# Page Configuration
# --------------------------------

st.set_page_config(
    page_title="Web Security Audit Toolkit",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #1e293b 100%
    );
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #020617;
    border-right: 1px solid #334155;
}

/* Cards */
div[data-testid="stMetric"] {
    background-color: #111827;
    border: 1px solid #334155;
    padding: 20px;
    border-radius: 16px;
}

/* Headers */
h1, h2, h3 {
    color: #f8fafc;
}

/* Buttons */
.stButton button {
    width: 100%;
    border-radius: 12px;
    height: 3rem;
    font-weight: bold;
}

/* Dataframes */
[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
}

/* Inputs */
.stTextInput input {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# Sidebar Navigation
# --------------------------------
st.sidebar.markdown("""
# 🛡️ SentinelShield

Cybersecurity Platform
""")
tool = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Login",
        "Register",
        "Website Audit",
        "Audit History",
        "Steganography"
    ]
)

# Show logged in user

if st.session_state["user"]:

    st.sidebar.success(
        f"Hello, {st.session_state['user']['name']}"
    )

    if st.sidebar.button("Logout"):

        st.session_state["user"] = None

        st.rerun()

if tool == "Dashboard":

    dashboard_page()

# =====================================
# LOGIN PAGE
# =====================================

elif tool == "Login":

    login_page()

# =====================================
# REGISTER PAGE
# =====================================

elif tool == "Register":

    register_page()

# =====================================
# WEBSITE AUDIT PAGE
# =====================================

elif tool == "Website Audit":

    # Protect page

    if not st.session_state["user"]:

        st.warning(
            "🔒 Please login to access Website Audit"
        )

        st.stop()

    st.title("🛡️ Website Security Intelligence Platform")

    url = st.text_input(
        "Enter Website URL",
        placeholder="https://example.com"
    )

    if st.button("Run Audit"):

        if url:

            with st.spinner("Running Security Audit..."):

                recon = get_website_info(url)

                ssl_info = get_ssl_info(url)

                headers = check_security_headers(url)

                findings = analyze_headers(headers)

                links = crawl_internal_links(url)

                page_results = audit_multiple_pages(
                    links
                )

                risk_score = calculate_risk_score(
                    findings
                )

                save_audit(
                    st.session_state["user"]["email"],
                    url,
                    risk_score
                )

                high, medium, low = (
                    count_severities(findings)
                )

                report_path = generate_report(
                    url,
                    recon,
                    ssl_info,
                    headers,
                    findings
                )

                pdf_path = generate_pdf_report(
                    url,
                    recon,
                    ssl_info,
                    headers,
                    findings
                )

            st.success("Audit Completed!")
            
            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
                "📊 Overview",
                "🔍 Recon",
                "🔒 SSL",
                "🛡️ Headers",
                "⚠️ Findings",
                "📄 Report"
            ])
            # SECURITY OVERVIEW
            with tab1:
                st.header("📊 Security Overview")

                col1, col2, col3, col4 = st.columns(4)

                col1.metric(
                    "Risk Score",
                    f"{risk_score}/100"
                )

                col2.metric(
                    "High",
                    high
                )

                col3.metric(
                    "Medium",
                    medium
                )

                col4.metric(
                    "Low",
                    low
                )

            # RECON
            with tab2:
                st.header("🔍 Reconnaissance")

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Status Code",
                    recon.get("Status Code", "N/A")
                )

                col2.metric(
                     "Server",
                     recon.get("Server", "Unknown")
                )

                col3.metric(
                     "Domain",
                     recon.get("Domain", "Unknown")
                )

                st.info(
                     recon.get(
                         "Title",
                         "Unknown"
                    )
                )

            # INTERNAL PAGES

                st.header(
                     "🌐 Internal Pages Found"
                    )

                if links:

                      for link in links:

                          st.write(link)

            # MULTI PAGE AUDIT

                st.header(
                     "📑 Multi-Page Security Audit"
                )

                for page in page_results:

                   st.subheader(
                      page["url"]
                 )

                if "error" in page:

                    st.error(
                        page["error"]
                    )

                else:

                    st.write(
                        f"Findings: {len(page['findings'])}"
                    )

            # SSL
            with tab3:
                st.header(
                    "🔒 SSL Analysis"
                )

                st.json(ssl_info)

            # HEADERS
            with tab4:
                st.header(
                    "🛡️ Security Headers"
                )

                st.json(headers)

            # FINDINGS TABLE
            with tab5:
                st.header(
                    "⚠️ Findings Dashboard"
                )

                if findings:

                    df = pd.DataFrame([
                      {
                        "Severity":
                        f["Severity"],

                        "Finding":
                        f["Header"],

                        "Recommendation":
                        f["Recommendation"]
                    }
                      for f in findings
                  ])

                    st.dataframe(
                        df,
                        use_container_width=True
                    )

                else:

                    st.success(
                        "No Findings Detected"
                    )

            # PDF
            with tab6:
                st.header(
                    "📄 Generated Report"
                )

                with open(
                    pdf_path,
                    "rb"
                ) as file:

                    st.download_button(
                        label="📥 Download Report",
                        data=file,
                        file_name="Security_Audit_Report.pdf",
                        mime="application/pdf"
                    )

        else:

            st.error(
                "Please enter a valid URL"
            )
#AUDIT HISTORY PAGE

elif tool == "Audit History":

    if not st.session_state["user"]:

        st.warning(
            "🔒 Please login first"
        )

        st.stop()

    st.title(
        "📜 Audit History"
    )

    audits = get_audits(
        st.session_state["user"]["email"]
    )

    if audits:

        df = pd.DataFrame([
            {
                "Website URL": a.website_url,
                "Risk Score": a.risk_score,
                "Date": a.created_at
            }
            for a in audits
        ])

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No audit history found"
        )
# =====================================
# STEGANOGRAPHY
# =====================================

elif tool == "Steganography":

    st.title("🖼️ Steganography Tool")

    st.success("Page Loaded Successfully")

    render_steganography()