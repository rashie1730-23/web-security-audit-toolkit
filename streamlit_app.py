import streamlit as st

from modules.recon import get_website_info
from modules.ssl_check import get_ssl_info
from modules.headers_check import check_security_headers
from modules.risk_analyzer import analyze_headers
from modules.report_generator import generate_report


st.set_page_config(
    page_title="Web Security Audit Toolkit",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Web Security Audit Toolkit")

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

            report_path = generate_report(
                url,
                recon,
                ssl_info,
                headers,
                findings
            )

        st.success("Audit Completed!")

        st.header("Reconnaissance")

        st.json(recon)

        st.header("SSL Analysis")

        st.json(ssl_info)

        st.header("Security Headers")

        st.json(headers)

        st.header("Findings")

        if findings:

            for finding in findings:

                st.warning(
                    f"{finding['Severity']} - "
                    f"{finding['Header']}"
                )

                st.write(
                    finding['Recommendation']
                )

        else:
            st.success("No Findings Detected")

        st.header("Generated Report")

        st.code(report_path)

    else:
        st.error("Please enter a valid URL")