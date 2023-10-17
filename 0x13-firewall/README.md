# Project Name: Firewall Configuration

## Introduction
Welcome to the Firewall Configuration project! In this project, you will be working with firewalls and network configurations to enhance the security and accessibility of your servers. Please follow the instructions carefully and have fun experimenting with the firewall settings.

## Project Details
- **Project Type:** DevOps, SysAdmin, Security
- **Author:** Sylvain Kalache, co-founder at Holberton School
- **Weight:** 1
- **Project Start:** October 16, 2023, 6:00 AM
- **Project End:** October 17, 2023, 6:00 AM
- **Checker Release:** October 16, 2023, 12:00 PM

## Concepts
In this project, the key concept to understand is **Web stack debugging**. Familiarize yourself with the basics of firewalls and how they function in a networked environment.

## Background Context
Imagine your servers without a firewall... Scary, right? This project will guide you in setting up a firewall using `ufw` (Uncomplicated Firewall) to control incoming traffic, allowing only specific TCP ports.

## Resources
Before you begin, make sure to go through the following resources:
- [What is a firewall](#) (link to relevant resource)
- [More Info](#) (additional reading material)

## Task Details

### Task 0: Block all incoming traffic but
**Description:** Install `ufw` firewall and configure it on `web-01`. The firewall should block all incoming traffic except for the following TCP ports: 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP). Ensure that you share the `ufw` commands you used in your answer file.

- **Repository:** alx-system_engineering-devops
- **Directory:** 0x13-firewall
- **File:** 0-block_all_incoming_traffic_but

### Task 1: Port Forwarding (Advanced)
**Description:** Firewalls not only filter requests but can also forward them. Configure `web-01` so that its firewall redirects incoming traffic on port 8080/TCP to port 80/TCP. Your answer file should contain a copy of the modified `ufw` configuration file that enables this port forwarding functionality.

- **Repository:** alx-system_engineering-devops
- **Directory:** 0x13-firewall
- **File:** 100-port_forwarding

## Important Notes
1. **Use caution:** Be very careful when modifying firewall rules. Mistakes can lead to loss of access to your server.
2. **Outside testing:** When testing on `web-01`, perform tests from outside the school network, for example, using your `web-02` server. SSH into your `web-02` server to bypass the school network firewall.
3. **Container Limitation:** Containers on demand cannot be used for this project due to Docker container limitations.

