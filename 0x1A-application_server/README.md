## Application Server Setup Project

## Overview
This project entails setting up an application server and integrating it with Nginx to serve multiple web applications and APIs. The tasks involve configuring servers, installing necessary tools, and ensuring seamless communication between components to achieve the desired functionality.

## Project Details
- **Authors:** Sylvain Kalache, co-founder at Holberton School
- **Project Weight:** 1
- **Project Start:** November 13, 2023 6:00 AM
- **Project End:** November 17, 2023 6:00 AM
- **Checker Release:** November 15, 2023 8:24 PM

## Concepts Covered
- Web Server
- Server
- Web stack debugging

## Background Context
The existing web infrastructure serves web pages through Nginx. The aim is to enhance this setup by incorporating an application server, enabling the serving of dynamic content and APIs for various Airbnb clone projects.

## Tasks Overview
- **Task 0:** Setting up Python development environment and configuring Flask to serve content on web-01.
- **Task 1:** Configuring production with Gunicorn to serve content from the same route and port as the development environment.
- **Task 2:** Serving a page with Nginx by configuring it to proxy requests to the Gunicorn instance.
- **Task 3:** Expanding the web application by configuring Nginx to proxy requests to another Gunicorn instance on a different port and route.
- **Task 4:** Serving the RESTful API by setting up Nginx to route requests to a Gunicorn instance.
- **Task 5:** Serving web dynamic content, ensuring proper handling of static assets via Nginx configuration.

## Resources
- Application server vs. web server
- Flask application setup with Gunicorn and Nginx on Ubuntu 16.04
- Upstart documentation

## Requirements
- Ubuntu 16.04 LTS compatibility
- Proper naming conventions and configurations in Bash scripts
- Comments in configuration files
- Execution permissions for Bash scripts
- Compatibility with specified versions of tools
- Functional Nginx configuration for proxying requests to Gunicorn instances

## Notes
This project requires a strong understanding of server configuration, Nginx, Flask, Gunicorn, and troubleshooting techniques to ensure successful implementation. All tasks build upon one another, expanding the functionality and complexity of the setup.

## Conclusion
Completing this project involves meticulous setup, configuration, and testing to ensure seamless integration between the application server and Nginx for serving various web applications and APIs.

