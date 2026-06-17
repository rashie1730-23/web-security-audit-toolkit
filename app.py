from modules.recon import get_website_info
from modules.ssl_check import get_ssl_info
from modules.headers_check import check_security_headers
from modules.risk_analyzer import analyze_headers
from modules.form_discovery import discover_forms

url = input("Enter Website URL: ")

print("\n===== RECON =====")
recon = get_website_info(url)

for k, v in recon.items():
    print(f"{k}: {v}")

print("\n===== SSL INFO =====")
ssl_info = get_ssl_info(url)

for k, v in ssl_info.items():
    print(f"{k}: {v}")

print("\n===== SECURITY HEADERS =====")
headers = check_security_headers(url)

for key, value in headers.items():
    print(f"{key}: {value}")

print("\n===== FINDINGS =====")
findings = analyze_headers(headers)

for finding in findings:
    print(f"\nHeader: {finding['Header']}")
    print(f"Severity: {finding['Severity']}")
    print(f"Recommendation: {finding['Recommendation']}")

print("\n===== FORM DISCOVERY =====")
forms = discover_forms(url)

if len(forms) == 0:
    print("No forms found.")

for form in forms:
    print(form)