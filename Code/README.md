This folder contains the necessary files for running the web server and associated scripts. It includes HTML files, PHP scripts, server configuration files, and security certificates.

# Contents:
- `files/`: Directory containing HTML and PHP files for the web application.
- `cert.pem`: SSL certificate file for HTTPS encryption.
- `key.pem`: SSL key file for HTTPS encryption.
- `server.py`: Main Python script for running the web server.
- `handle_req.py`: Python script for processing incoming requests.
- `parse_req.py`: Python script for parsing requests.
- `make_resp.py`: Python script for generating responses.
- `php_utils.py`: Utility script for PHP-related operations.
- `exception.py`: Python script for handling exceptions.


# Dependencies
To run the scripts in this folder, the following dependencies are required:

## Python 3
```bash
sudo apt-get update 
sudo apt-get install python3 
```

## PHP-CGI
```bash
sudo apt-get install php-cgi 
```


# Usage
To start the web server locally on port 443, execute the server.py script. 
```bash 
sudo python3 server.py localhost 443 cert.pem key.pem 
```


# Executing Requests
GET and POST can be tested via browser or curl.
## GET Request
To fetch data from the server. 
```bash 
curl https://localhost/get_req.php?name=value1&email=value2 
```

## POST Request
To send data to the server.
```bash 
curl -X POST -d "email=value1&password=value2" https://localhost/post_req.php 
```

## PUT Request
To update data on the server. 
```bash 
curl -X PUT -d "This is a test" https://localhost/myfile.txt 
```

## DELETE Request
To delete data on the server. 
```bash 
curl -X DELETE https://localhost/myfile.txt 
```

