import requests
from bs4 import BeautifulSoup


def discover_forms(url):
    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        forms = soup.find_all("form")

        discovered_forms = []

        for index, form in enumerate(forms, start=1):
            discovered_forms.append({
                "Form Number": index,
                "Action": form.get("action", "Not Specified"),
                "Method": form.get("method", "GET").upper(),
                "Inputs": len(form.find_all("input"))
            })

        return discovered_forms

    except Exception as e:
        return [{"Error": str(e)}]