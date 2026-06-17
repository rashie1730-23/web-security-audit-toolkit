import requests


def check_security_headers(url):
    try:
        response = requests.get(url, timeout=10)

        security_headers = {
            "Content-Security-Policy": response.headers.get(
                "Content-Security-Policy", "Missing"
            ),
            "Strict-Transport-Security": response.headers.get(
                "Strict-Transport-Security", "Missing"
            ),
            "X-Frame-Options": response.headers.get(
                "X-Frame-Options", "Missing"
            ),
            "X-Content-Type-Options": response.headers.get(
                "X-Content-Type-Options", "Missing"
            ),
            "Referrer-Policy": response.headers.get(
                "Referrer-Policy", "Missing"
            ),
            "Permissions-Policy": response.headers.get(
                "Permissions-Policy", "Missing"
            )
        }

        return security_headers

    except Exception as e:
        return {"Error": str(e)}