import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_website_info(url):
    try:
        # Send request to website
        response = requests.get(url, timeout=10)

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract title
        title = soup.title.string.strip() if soup.title else "No Title Found"

        # Extract domain
        parsed_url = urlparse(url)

        # Collect information
        website_info = {
            "Domain": parsed_url.netloc,
            "Title": title,
            "Status Code": response.status_code,
            "Server": response.headers.get("Server", "Unknown"),
            "Content Type": response.headers.get("Content-Type", "Unknown"),
            "URL": url
        }

        return website_info

    except requests.exceptions.RequestException as e:
        return {
            "Error": str(e)
        }


# Test Run
if __name__ == "__main__":
    url = input("Enter Website URL: ")

    result = get_website_info(url)

    print("\n===== Website Information =====\n")

    for key, value in result.items():
        print(f"{key}: {value}")