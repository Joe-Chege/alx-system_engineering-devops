0x0C. Web server

# Web Server

## Background Context

In this project, some of the tasks will be graded on two aspects:

1. Is your web-01 server configured according to requirements?
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)?

For example, if I need to create a file `/tmp/test` containing the string "hello world" and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use `emacs` on my server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`.

But my answer file would contain:

```bash
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
```

As you can tell, I am not using `emacs` to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage; the work cannot be only done manually. Note that the checker will execute your script as the root user, and you do not need to use the `sudo` command.

A good Software Engineer is a lazy Software Engineer.

**Tips:** To test your answer Bash script, feel free to reproduce the checker's environment:

- Start an Ubuntu 16.04 sandbox.
- Run your script on it.
- See how it behaves.

### Resources

**Read or watch:**

- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://www.nginx.com/resources/glossary/nginx/)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-on-ubuntu-20-04)
- [Child process concept page](https://en.wikipedia.org/wiki/Child_process)
- [Root and subdomain](https://en.wikipedia.org/wiki/Subdomain)
- [HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [HTTP redirection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections)
- [Not found HTTP response code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404)
- [Log files on Linux](https://www.tecmint.com/20-funny-commands-of-linux-or-linux-is-fun-in-terminal/)

**For reference:**

- [RFC 7231 (HTTP/1.1)](https://tools.ietf.org/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://tools.ietf.org/html/rfc7540)

**Man or help:**

- `scp`
- `curl`

### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General:**

- What is the main role of a web server?
- What is a child process?
- Why do web servers usually have a parent process and child processes?
- What are the main HTTP requests?

**DNS:**

- What DNS stands for.
- What is DNS's main role.
- DNS Record Types:
  - A
  - CNAME
  - TXT
  - MX

### Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives.

You will not be able to meet the objectives of this or any following project by copying and pasting someone else's work.

You are not allowed to publish any content of this project.

Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

**General:**

- Allowed editors: `vi`, `vim`, `emacs`.
- All your files will be interpreted on Ubuntu 16.04 LTS.
- All your files should end with a new line.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- All your Bash script files must be executable.
- Your Bash script must pass Shellcheck (version 0.3.7) without any error.
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of all your Bash scripts should be a comment explaining what the script is doing.
- You can't use `systemctl` for restarting a process.