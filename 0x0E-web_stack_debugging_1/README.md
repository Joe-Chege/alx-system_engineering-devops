## Project Title

Web Stack Debugging 1 - Fixing Nginx Listening on Port 80

## Project Description

This project aims to solve an issue with an Nginx installation on an Ubuntu 20.04 LTS server that prevents it from listening on port 80. The task involves debugging the issue, finding a solution, and creating Bash scripts to automate the fix. The solution must meet specific requirements outlined in the task description.

## Project Structure

The project repository (`alx-system_engineering-devops`) contains the following directory and files:

- **Directory**: `0x0E-web_stack_debugging_1`
- **Files**:
  1. `0-nginx_likes_port_80`: Bash script to fix the Nginx installation and make it listen on port 80.
  2. `1-debugging_made_short`: Bash script containing a shorter and more concise version of the fix for Nginx listening on port 80.

## Requirements

### General

- **Editors**: vi, vim, emacs
- **Operating System**: Ubuntu 20.04 LTS
- **File Endings**: All files should end with a new line
- **Documentation**: A `README.md` file at the root of the project folder is mandatory.
- **Executable Scripts**: All Bash script files must be executable.
- **Shellcheck**: Bash scripts must pass Shellcheck without any errors.
- **Script Execution**: Bash scripts must run without errors.
- **Script Headers**: The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- **Comments**: The second line of all Bash scripts should be a comment explaining what the script is doing.
- **Restrictions**: Do not use `wget`.
  
### Task 0: Nginx likes port 80

- **Fix Requirement**: Nginx must be running and listening on port 80 of all the server’s active IPv4 IPs.
- **Script**: Write a Bash script that configures the server to meet the above requirements.

### Task 1: Make it sweet and short

- **Fix Requirement**: Nginx should be fixed to listen on port 80.
- **Script**: Create a Bash script that accomplishes the task within 5 lines, following the specified conditions (no use of `;`, `&&`, `wget`; service must report that nginx is not running).

## How to Run the Scripts

1. **Task 0 Script**:
   ```bash
   ./0-nginx_likes_port_80
   ```
   This script will fix the Nginx installation to listen on port 80.

2. **Task 1 Script**:
   ```bash
   ./1-debugging_made_short
   ```
   This shorter version of the fix will also ensure Nginx listens on port 80.

## Additional Notes

- Please ensure that the system meets the specified requirements before running the scripts.
- If you encounter any issues or have questions, feel free to reach out for assistance.

---