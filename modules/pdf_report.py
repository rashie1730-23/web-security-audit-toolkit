from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    url,
    recon,
    ssl_info,
    headers,
    findings
):

    pdf_path = "reports/security_audit_report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Web Security Audit Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Target Website: {url}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Reconnaissance",
            styles["Heading2"]
        )
    )

    for key, value in recon.items():
        content.append(
            Paragraph(
                f"{key}: {value}",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "SSL Analysis",
            styles["Heading2"]
        )
    )

    for key, value in ssl_info.items():
        content.append(
            Paragraph(
                f"{key}: {value}",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Security Headers",
            styles["Heading2"]
        )
    )

    for key, value in headers.items():
        content.append(
            Paragraph(
                f"{key}: {value}",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Findings",
            styles["Heading2"]
        )
    )

    for finding in findings:
        content.append(
            Paragraph(
                f"{finding['Severity']} - "
                f"{finding['Header']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                finding["Recommendation"],
                styles["Normal"]
            )
        )

    doc.build(content)

    return pdf_path