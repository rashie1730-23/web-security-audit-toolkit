from datetime import datetime


def generate_report(url, recon, ssl_info, headers, findings):
    report_name = "reports/audit_report.md"

    with open(report_name, "w", encoding="utf-8") as report:

        report.write("# Web Security Audit Report\n\n")

        report.write(f"Generated: {datetime.now()}\n\n")

        report.write(f"## Target Website\n")
        report.write(f"{url}\n\n")

        report.write("## Reconnaissance\n\n")

        for key, value in recon.items():
            report.write(f"- **{key}**: {value}\n")

        report.write("\n## SSL Analysis\n\n")

        for key, value in ssl_info.items():
            report.write(f"- **{key}**: {value}\n")

        report.write("\n## Security Headers\n\n")

        for key, value in headers.items():
            report.write(f"- **{key}**: {value}\n")

        report.write("\n## Findings\n\n")

        if len(findings) == 0:
            report.write("No findings detected.\n")

        for finding in findings:
            report.write(
                f"- **{finding['Severity']}** | "
                f"{finding['Header']} | "
                f"{finding['Recommendation']}\n"
            )

    return report_name