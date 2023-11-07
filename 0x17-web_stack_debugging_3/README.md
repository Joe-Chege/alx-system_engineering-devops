# Web Stack Debugging #3

This project focuses on debugging a WordPress website that is running on a LAMP (Linux, Apache, MySQL, PHP) stack. The task involves using `strace` to identify and resolve a 500 Internal Server Error returned by the Apache web server. After manually fixing the issue, the solution is automated using Puppet, a configuration management tool.

## Project Objective

The main objective of this project is to:

1. **Identify the Issue:** Use `strace` to trace system calls and diagnose the root cause of the 500 Internal Server Error.
2. **Manual Fix:** Manually fix the identified issue on the Apache server to resolve the error.
3. **Automation:** Automate the fix using Puppet, ensuring that the solution can be applied automatically.

## Prerequisites

- This project assumes you have access to a server running Ubuntu 14.04 LTS.
- Ensure that `strace` and Puppet are installed on your system.

## Project Tasks

### Step 1: Identify the Issue Using `strace`

1. **Run Apache with `strace`:**
   - Stop Apache service:
     ```bash
     sudo service apache2 stop
     ```
   - Run Apache with `strace` and save the output to a file:
     ```bash
     sudo strace -f -o strace_output.txt /usr/sbin/apache2 -X
     ```

2. **Reproduce the Issue:**
   - Trigger the 500 Internal Server Error by accessing the WordPress website.

3. **Analyze `strace` Output:**
   - Examine `strace_output.txt` to identify system calls and pinpoint the issue causing the error.

### Step 2: Fix the Issue Manually

1. **Identify the Problem:**
   - Based on `strace` output, determine the root cause of the error (e.g., file permissions, missing file).

2. **Implement a Manual Fix:**
   - Apply a manual fix to resolve the identified problem.

3. **Verify the Fix:**
   - Restart Apache and confirm that the WordPress website loads without errors.

### Step 3: Automate the Fix Using Puppet

1. **Create a Puppet Manifest:**
   - Create a new Puppet manifest file (e.g., `0-strace_is_your_friend.pp`).

2. **Write Puppet Code:**
   - Write Puppet code to automate the manual fix. Use appropriate Puppet resource types like `file`, `exec`, or `service`.

3. **Apply the Puppet Manifest:**
   - Apply the Puppet manifest to automate the fix:
     ```bash
     sudo puppet apply 0-strace_is_your_friend.pp
     ```

4. **Verify the Automated Fix:**
   - Test the WordPress website to ensure the issue is resolved through Puppet automation.

## Project Structure

- `0-strace_is_your_friend.pp`: Puppet manifest file containing the automated fix.
- `strace_output.txt`: Output file containing `strace` system call traces.

## Additional Notes

- Document any specific issues encountered, the steps taken to diagnose the problem, and the solutions applied.
- Include relevant code snippets and explanations in the README for reference.
