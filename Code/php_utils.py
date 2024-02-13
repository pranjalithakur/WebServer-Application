import subprocess
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# Default environment variables for CGI execution
DEFAULT_ENV_VARS = {
    "QUERY_STRING": "",
    "SCRIPT_NAME": "",
    "SCRIPT_FILENAME": "",
    "REQUEST_METHOD": "",
    "GATEWAY_INTERFACE": "CGI/1.1",
    "REDIRECT_STATUS": '0',
    "CONTENT_TYPE": 'application/x-www-form-urlencoded',
    "CONTENT_LENGTH": '0',
    "REMOTE_HOST": ""
}

def ExecutePHP(php_path, request, address):
    env_vars = DEFAULT_ENV_VARS.copy()  
    
    if request["method"] == "GET":
        env_vars["REQUEST_METHOD"] = "GET"
    elif request["method"] == "POST":
        env_vars["REQUEST_METHOD"] = "POST"
        env_vars["CONTENT_LENGTH"] = str(len(request["body"]))
        if "content-type" in request["headers"].keys():
            env_vars["CONTENT_TYPE"] = request["headers"]["content-type"]

    env_vars["SCRIPT_NAME"] = php_path.name
    env_vars["SCRIPT_FILENAME"] = str(php_path)
    if "request_uri_query" in request.keys():
        env_vars["QUERY_STRING"] = request["request_uri_query"]
    env_vars["REMOTE_HOST"] = address[0]

    if env_vars["REQUEST_METHOD"] == "POST":
        # Handling POST request by invoking 'php-cgi' with input from request body
        post_process = subprocess.Popen(["php-cgi"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env_vars)
        (post_script_output, post_script_errors) = post_process.communicate(input=request["body"].encode())
        return post_script_output

	# Handling GET request by invoking 'php-cgi'
    get_process = subprocess.Popen(["php-cgi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env_vars)
    get_script_output = get_process.stdout.read()
    get_script_errors = get_process.stderr.read()
    return get_script_output