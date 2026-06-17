def count_severities(findings):

    high = 0
    medium = 0
    low = 0

    for finding in findings:

        if finding["Severity"] == "High":
            high += 1

        elif finding["Severity"] == "Medium":
            medium += 1

        elif finding["Severity"] == "Low":
            low += 1

    return high, medium, low