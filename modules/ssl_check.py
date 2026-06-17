import ssl
import socket
from urllib.parse import urlparse


def get_ssl_info(url):
    try:
        hostname = urlparse(url).hostname

        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        return {
            "SSL Enabled": True,
            "Issuer": dict(x[0] for x in cert["issuer"]),
            "Valid From": cert["notBefore"],
            "Valid Until": cert["notAfter"]
        }

    except Exception as e:
        return {
            "SSL Enabled": False,
            "Error": str(e)
        }