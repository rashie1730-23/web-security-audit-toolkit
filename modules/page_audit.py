from modules.headers_check import check_security_headers
from modules.risk_analyzer import analyze_headers


def audit_multiple_pages(links):

    results = []

    for link in links:

        try:

            headers = check_security_headers(link)

            findings = analyze_headers(headers)

            results.append({
                "url": link,
                "headers": headers,
                "findings": findings
            })

        except Exception as e:

            results.append({
                "url": link,
                "error": str(e)
            })

    return results