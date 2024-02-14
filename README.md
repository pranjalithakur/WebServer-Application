# Secure Web Application Server with Docker Deployment

This project involves a comprehensive web server setup using Docker, including a custom Python-based web server and an Nginx reverse proxy configured for HTTPS. The web server is designed to handle both static content and PHP scripts, with the latter being processed through a PHP interpreter.

Additionally, the setup includes load balancing capabilities, distributing incoming traffic across multiple instances of the web server. For testing purposes, a Selenium environment within a Docker container is established to exploit and test a path traversal vulnerability in the web server. 


## Objective
The primary goal of this project was to develop a highly secure web application server, specifically tailored for PHP script execution. The server was designed to be deployed using Docker, ensuring both security and scalability. A key focus was on mitigating common web vulnerabilities such as SQL injections and path traversal, with an emphasis on handling web requests securely.


### Skills Learned
[Bullet Points]

- Mastery in Docker containerization and deployment techniques, ensuring a scalable and secure server environment.
- Advanced understanding and application of web security principles, particularly in parsing and handling HTTP requests.
- Proficiency in implementing security measures against common vulnerabilities like SQL injections and path traversal attacks.
- Enhanced skills in vulnerability testing and documentation, using tools like Selenium for automated testing.


### Tools Used
[Bullet Points]

- Docker: Used for containerizing the web application server, facilitating easy deployment and scalability.
- PHP: Selected for script execution within the web server environment.
- Selenium: Employed for automated vulnerability testing to ensure robust security.
- Various Security Tools: Utilized for mitigating risks such as SQL injections and path traversal vulnerabilities.


## Steps
[Bullet Points]

- Writing a Parser: Developed a parser for HTTP requests without using external libraries, focusing on understanding the structure of HTTP requests and ensuring their validation.
- Turning the Parser into a Server: Integrated the parser with networking and file access modules to create a functional HTTP server. Emphasis was on making the server accessible to a network and serving files securely.
- Adding Server-side Execution: Enhanced the server by enabling PHP scripting, ensuring dynamic content delivery. Special attention was given to correctly populating $_GET and $_POST arrays in PHP.
- Vulnerability Testing: Conducted rigorous tests using Selenium scripts to identify and mitigate any potential security vulnerabilities.
- Documentation: Methodically documented the entire development process, including the configuration and deployment steps, as well as the findings from the vulnerability tests.
- Deployment with Docker: Finalized the project by deploying the server using Docker, emphasizing on security and scalability in a containerized environment.
