# 🛡️ Web Security Audit Toolkit

A comprehensive cybersecurity auditing platform built using Python and Streamlit that automates website security assessments, vulnerability identification, SSL analysis, security header validation, risk scoring, report generation, and steganography operations.

---

## 📌 Project Overview

This project was developed as part of a Cybersecurity Internship to perform automated security audits on web applications and identify potential security weaknesses.

The toolkit allows users to:

* Analyze website security configurations
* Verify SSL/TLS certificate implementation
* Detect missing security headers
* Perform reconnaissance and information gathering
* Discover internal website pages
* Conduct multi-page security assessments
* Generate downloadable PDF security reports
* Encode and decode secret messages using steganography

---

## 🚀 Features

### 🔍 Website Reconnaissance

* Domain Identification
* Website Title Extraction
* Server Information Detection
* HTTP Status Analysis

### 🔒 SSL Certificate Analysis

* SSL Verification
* Certificate Issuer Information
* Certificate Validity Check
* Expiration Monitoring

### 🛡️ Security Header Assessment

* Content-Security-Policy (CSP)
* Strict-Transport-Security (HSTS)
* X-Frame-Options
* X-Content-Type-Options
* Referrer-Policy
* Permissions-Policy

### 📊 Risk Analysis Engine

* Vulnerability Severity Classification
* Security Score Calculation
* Risk Dashboard
* Findings Prioritization

### 🌐 Internal Link Discovery

* Website Crawling
* Internal Page Enumeration
* Multi-Page Security Assessment

### 📄 Report Generation

* PDF Security Reports
* Downloadable Findings
* Audit Documentation

### 🖼️ Steganography Module

* Message Encoding
* Message Decoding
* Image-Based Data Hiding

---

## 🏗️ Project Structure

```text
web-security-audit-toolkit/
│
├── modules/
│   ├── recon.py
│   ├── ssl_check.py
│   ├── headers_check.py
│   ├── crawler.py
│   ├── page_audit.py
│   ├── risk_analyzer.py
│   ├── risk_score.py
│   ├── severity_stats.py
│   ├── report_generator.py
│   └── pdf_report.py
│
├── steganography/
│   ├── encode.py
│   ├── decode.py
│   └── steg_ui.py
│
├── reports/
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Technology Stack

* Python 3.12
* Streamlit
* Requests
* BeautifulSoup4
* ReportLab
* Pillow
* Pandas

---

## 🖥️ Installation

Clone the repository:

```bash
git clone https://github.com/rashie1730-23/web-security-audit-toolkit.git
cd web-security-audit-toolkit
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run streamlit_app.py
```

---

## 📈 Security Audit Workflow

1. Enter target website URL
2. Perform reconnaissance
3. Analyze SSL certificate
4. Validate security headers
5. Discover internal pages
6. Execute multi-page assessment
7. Calculate risk score
8. Generate findings
9. Download PDF report

---

## 🎯 Internship Objectives Covered

✅ Website Security Assessment

✅ SSL/TLS Analysis

✅ Security Header Validation

✅ Vulnerability Identification

✅ Risk Assessment

✅ Security Reporting

✅ Multi-Page Security Audit

✅ Steganography Implementation

---

## 🔮 Future Enhancements

* OWASP Top 10 Detection
* Login Form Analysis
* SQL Injection Testing
* XSS Detection
* Authentication Review
* API Security Assessment
* Export to Excel
* Interactive Security Dashboard

---

## 👩‍💻 Author

**Rashi Manjrekar**

Electronics & Computer Science Engineering Student

Cybersecurity Intern

---

## 📜 License

This project is licensed under the MIT License.
