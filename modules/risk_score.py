def calculate_risk_score(findings):

    score = 100

    for finding in findings:

        severity = finding["Severity"]

        if severity == "High":
            score -= 20

        elif severity == "Medium":
            score -= 10

        elif severity == "Low":
            score -= 5

    return max(score, 0)