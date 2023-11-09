# Webstack Monitoring Project

## Overview

This project focuses on web stack monitoring, an essential aspect of managing software systems and servers. The goal is to implement effective monitoring using Datadog, a popular monitoring service. By setting up monitors and dashboards, you can gain insights into your systems' performance and receive alerts if any issues arise.

## Tasks

### Task 0: Sign up for Datadog and Install Datadog Agent

- Sign up for a free Datadog account on the [Datadog website](https://www.datadoghq.com/).
- Install the Datadog agent on `web-01`.
- Create an application key and API key.
- Ensure server `web-01` is visible in Datadog under the hostname `XX-web-01`.

### Task 1: Monitor Some Metrics

- Set up a monitor to check the number of read requests issued to the device per second.
- Set up a monitor to check the number of write requests issued to the device per second.

### Task 2: Create a Dashboard

- Create a new dashboard on Datadog.
- Add at least 4 widgets to your dashboard, monitoring various metrics.
- Create a file named `2-setup_datadog` containing the `dashboard_id` on the first line.

## Project Structure

- **`0-sign_up_for_datadog.sh`**: Bash script for signing up for Datadog, installing the agent, and configuring keys.
- **`1-monitor_metrics.sh`**: Bash script for setting up monitors to track read and write requests.
- **`2-setup_datadog`**: Text file containing the `dashboard_id` for Task 2.

## How to Run the Scripts

1. **Task 0:**
   - Run `0-sign_up_for_datadog.sh` on your local machine or server.
   - Follow the prompts to sign up for Datadog, install the agent, and configure keys.

2. **Task 1:**
   - Run `1-monitor_metrics.sh` on your local machine or server.
   - This script sets up monitors for read and write requests.

## Dashboard Information

- Access your Datadog account to view the created dashboard.
- The dashboard contains widgets displaying various metrics related to your servers and applications.

## Notes

- Ensure that you have the necessary permissions and privileges to perform the tasks.
- For any issues or questions, please refer to the project guidelines or seek assistance from your supervisor or team.

---

**Copyright © 2023 ALX. All rights reserved.**