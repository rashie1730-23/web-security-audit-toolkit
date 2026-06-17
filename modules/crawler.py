import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl_internal_links(url):

    try:

        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        links = set()

        base_domain = urlparse(url).netloc

        for tag in soup.find_all("a", href=True):

            full_url = urljoin(url, tag["href"])

            parsed = urlparse(full_url)

            if parsed.netloc == base_domain:
                links.add(full_url)

        return list(links)

    except Exception as e:

        return [f"Error: {str(e)}"]