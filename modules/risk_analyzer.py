def analyze_headers(headers):
    findings = []

    risk_map = {
        "Content-Security-Policy": (
            "Medium",
            "Implement CSP to reduce XSS risks."
        ),
        "Strict-Transport-Security": (
            "High",
            "Enable HSTS to enforce HTTPS."
        ),
        "X-Frame-Options": (
            "Medium",
            "Prevent clickjacking attacks."
        ),
        "X-Content-Type-Options": (
            "Low",
            "Prevent MIME type sniffing."
        ),
        "Referrer-Policy": (
            "Low",
            "Limit information leakage."
        ),
        "Permissions-Policy": (
            "Low",
            "Restrict browser feature access."
        )
    }

    for header, value in headers.items():
        if value == "Missing":
            findings.append({
                "Header": header,
                "Severity": risk_map[header][0],
                "Recommendation": risk_map[header][1]
            })

    return findings