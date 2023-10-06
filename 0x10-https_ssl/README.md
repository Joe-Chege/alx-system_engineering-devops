# HTTPS SSL Project

This project focuses on securing website traffic using HTTPS SSL, integrating HAProxy for SSL termination. The goal is to ensure encrypted communication and enhance web security. 

## Project Details

- **Author:** Sylvain Kalache, co-founder at Holberton School
- **Project Start:** October 5, 2023, 6:00 AM
- **Project End:** October 6, 2023, 6:00 AM
- **Checker Release:** October 5, 2023, 12:00 PM

## Concepts Covered

- **DNS:** Domain Name System configuration.
- **Web Stack Debugging:** Troubleshooting and debugging web server setups.

## Background Context

Understanding the significance of securing website traffic and the consequences of not doing so.

## Learning Objectives

Upon completion, you are expected to comprehend:

- What HTTPS SSL is and its primary roles.
- The purpose of encrypting traffic.
- Meaning and significance of SSL termination.

## Requirements

- **Editors:** vi, vim, emacs.
- **Environment:** Ubuntu 16.04 LTS.
- **Line Endings:** All files should end with a newline character.
- **File Structure:** Include a `README.md` file at the project's root folder.
- **Bash Scripts:** All scripts must be executable, pass Shellcheck (version 0.3.7) without errors, and have the appropriate shebang (`#!/usr/bin/env bash`).
- **Script Comments:** Include a comment as the second line in each Bash script, explaining the script's purpose.
- **Quiz:** Successfully complete the associated quiz.

## Project Tasks

### Task 0: World Wide Web

Configure your domain zone to point various subdomains to specific IP addresses. Create a Bash script that audits subdomains and displays relevant information.

**Requirements:**
- Add subdomains: `www`, `lb-01`, `web-01`, `web-02`.
- Bash script should accept domain and subdomain parameters.
- Output format: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`.

Example:
```
./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
```

### Task 1: HAProxy SSL Termination

Configure HAProxy to handle encrypted traffic (SSL termination) for the `www` subdomain. HAProxy must listen on TCP port 443 and serve encrypted traffic returning the root of your web server with "Holberton School".

**Requirements:**
- HAProxy version 1.5 or higher.
- HAProxy must serve encrypted traffic on port 443.
- The page returned for the root domain must contain "Holberton School".
- Provide HAProxy configuration in `1-haproxy_ssl_termination` file.

Example:
```
curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
...
```

---

**Repository Details:**
- **GitHub Repository:** alx-system_engineering-devops
- **Directory:** 0x10-https_ssl

For further instructions and updates, refer to the project's specific guidelines and resources provided. Good luck with your HTTPS SSL project!
