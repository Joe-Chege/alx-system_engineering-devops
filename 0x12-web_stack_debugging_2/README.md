# Web Stack Debugging #2

This repository contains solutions for the "Web stack debugging #2" project, a part of the ALX School curriculum.

## Project Overview

In this project, the goal is to fix a misconfigured web server running on a container. The main tasks include running software as another user and configuring Nginx to run as the `nginx` user.

## Project Structure

- `0-iamsomeoneelse`: Bash script to run the `whoami` command under the user passed as an argument.
- `1-run_nginx_as_nginx`: Bash script to configure Nginx to run as the `nginx` user and listen on all active IPs on port 8080.
- `100-fix_in_7_lines_or_less`: An advanced Bash script that achieves the same goal as task #1 in 7 lines or less.

## Task Details

### Task 0: Run software as another user

#### Description

The `0-iamsomeoneelse` script accepts one argument and runs the `whoami` command under the specified user.

#### Usage

```bash
./0-iamsomeoneelse <username>
```

### Task 1: Run Nginx as Nginx

#### Description

The `1-run_nginx_as_nginx` script configures Nginx to run as the `nginx` user, listening on all active IPs on port 8080.

#### Usage

```bash
./1-run_nginx_as_nginx
```

### Task 2: 7 lines or less

#### Description

The `100-fix_in_7_lines_or_less` script achieves the same goal as task #1 but in 7 lines or less, following specific constraints.

#### Usage

```bash
./100-fix_in_7_lines_or_less
```

## Notes

- All scripts are tested and verified to run on Ubuntu 20.04 LTS.
- Scripts adhere to Bash script requirements, ensuring they are executable, pass Shellcheck without errors, and run without issues.
- For security reasons, it's important to review and understand the scripts before running them in a production environment.

---

**Copyright © 2023 ALX, All rights reserved.**