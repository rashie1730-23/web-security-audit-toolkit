# Web Security Audit Report

Generated: 2026-06-17 09:22:40.831836

## Target Website
https://ccgac.bitrix24.site/

## Reconnaissance

- **Domain**: ccgac.bitrix24.site
- **Title**: Cloud Counselage Pvt. Ltd.
- **Status Code**: 200
- **Server**: Bitrix24.Sites
- **Content Type**: text/html; charset=UTF-8
- **URL**: https://ccgac.bitrix24.site/

## SSL Analysis

- **SSL Enabled**: True
- **Issuer**: {'countryName': 'US', 'stateOrProvinceName': 'Arizona', 'localityName': 'Scottsdale', 'organizationName': 'GoDaddy.com, Inc.', 'organizationalUnitName': 'http://certs.godaddy.com/repository/', 'commonName': 'Go Daddy Secure Certificate Authority - G2'}
- **Valid From**: Aug 10 13:48:54 2025 GMT
- **Valid Until**: Sep 11 13:48:54 2026 GMT

## Security Headers

- **Content-Security-Policy**: Missing
- **Strict-Transport-Security**: Missing
- **X-Frame-Options**: Missing
- **X-Content-Type-Options**: Missing
- **Referrer-Policy**: Missing
- **Permissions-Policy**: Missing

## Findings

- **Medium** | Content-Security-Policy | Implement CSP to reduce XSS risks.
- **High** | Strict-Transport-Security | Enable HSTS to enforce HTTPS.
- **Medium** | X-Frame-Options | Prevent clickjacking attacks.
- **Low** | X-Content-Type-Options | Prevent MIME type sniffing.
- **Low** | Referrer-Policy | Limit information leakage.
- **Low** | Permissions-Policy | Restrict browser feature access.
