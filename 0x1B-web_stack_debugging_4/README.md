# Web Stack Debugging Project

This project involves debugging and optimizing a web stack setup featuring Nginx under pressure using ApacheBench. The goal is to resolve failed requests and address user limit issues encountered during testing.

## Tasks Overview

### Task 0: Sky is the limit, let's bring that limit higher

- **Objective:** Fix failed requests during benchmarking.
- **Steps Taken:**
  - Investigated failed requests using ApacheBench.
  - Reviewed Nginx error logs (`/var/log/nginx/error.log`).
  - Modified Nginx configuration (`/etc/nginx/nginx.conf`) to accommodate more requests by adjusting worker processes, connections, or related settings.
  - Applied changes and retested using ApacheBench.
  - Created Puppet manifest (`0-the_sky_is_the_limit_not.pp`) to automate Nginx configuration changes.

### Task 1: User limit

- **Objective:** Resolve "Too many open files" error for the `holberton` user.
- **Steps Taken:**
  - Identified the issue with the user limit error.
  - Adjusted system configuration (`/etc/security/limits.conf`) to increase the maximum number of open files for users.
  - Developed Puppet manifest (`1-user_limit.pp`) to automate the user limit configuration for the `holberton` user.

## Project Structure

### Directory: `0x1B-web_stack_debugging_4`

- **Files:**
  - `0-the_sky_is_the_limit_not.pp`: Puppet manifest for Task 0.
  - `1-user_limit.pp`: Puppet manifest for Task 1.
  - *Add any other relevant files or directories here.*

## Usage

### Running Puppet Manifests

To apply the Puppet manifests and implement the fixes:

```bash
# Example commands for applying Puppet manifests
puppet apply 0-the_sky_is_the_limit_not.pp    # For Task 0
puppet apply 1-user_limit.pp                  # For Task 1
```

Ensure you have necessary permissions and review the changes made before executing Puppet manifests in a production environment.

## Notes

- Always test changes in a controlled environment before applying them to production.
- Backup critical configurations before making significant modifications.
- Document any changes made for reference and future troubleshooting.

