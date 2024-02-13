This folder contains Ansible playbooks and configurations for setting up and managing a web server environment. The setup is designed to automate the deployment and configuration of a web server.

# Contents:
- `playbook.yml`: The main Ansible playbook file. It defines tasks to be executed on the target servers.
- `web_server.service.j2`: Jinja2 template for the web server's systemd service file.
- `stop_service.yml`: Playbook for stopping the web server service.

# Dependencies
```bash
sudo apt install ansible 
```

# Usage
Execute the Ansible playbook to deploy and configure the web server.
## Deploying and Configuring the Web Server:
```bash
sudo ansible-playbook playbook.yml -i 'localhost,' -c local 
```

## Stopping the Web Server Service:
```bash
sudo ansible-playbook stop_service.yml 
```
