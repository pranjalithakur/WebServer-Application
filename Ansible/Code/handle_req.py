import logging
from pathlib import Path
import os
import parse_req
import php_utils
import make_resp

logger = logging.getLogger(__name__)

# Function to handle GET requests
def handle_get_request(request, address):
    # Creating paths for requested and current files
    requested_path = Path("usr/local/src/web_server/Code/files/" + request["request_uri_path"].strip('/')).resolve()
    current_path = Path("usr/local/src/web_server/Code/files").resolve()

    # If requested path is the root, set it to index.html
    if requested_path == current_path:
        requested_path = Path("usr/local/src/web_server/Code/files/index.html").resolve()

    # Handling cases when file is not found or inaccessible
    if not requested_path.is_file() or not requested_path.exists():
        try:
            # Trying to read and return contents of a file
            with open("./", 'r') as f:
                resp_body = f.read()
                resp_body = resp_body.encode()
                resp_body_headers = {"content-length": len(resp_body)}
                return make_resp.resp_gen(404, resp_body_headers, resp_body ) 
            
        except Exception as e:
            return make_resp.resp_gen(500)  
    
    # Checking if requested file is readable
    if not os.access(requested_path, os.R_OK):
        return make_resp.resp_gen(403)  
    
    # Handling PHP files differently
    if requested_path.suffix == '.php':
        resp_body = php_utils.ExecutePHP(requested_path, request, address)
        resp_body_headers = {"content-length": len(resp_body)}
        return make_resp.resp_gen(200, resp_body_headers, resp_body, body_headers=True)
    
    else:
        try:
            # Trying to read and return contents of a file
            with open(requested_path, 'r') as f:
                resp_body = f.read().encode()
                resp_body_headers = {"content-length": len(resp_body)}
                response = make_resp.resp_gen(200, resp_body_headers, resp_body)      
                return response
            
        except FileNotFoundError:
            return make_resp.resp_gen(404)
            
        except Exception:
            return make_resp.resp_gen(500) 


def handle_post_request(request, address):
    content_length = request['headers'].get('Content-Length')
   
    requested_path = Path("usr/local/src/web_server/Code/files/" + request["request_uri_path"].strip('/')).resolve()
    current_path = Path("usr/local/src/web_server/Code/files").resolve()

    # Checking if the requested path is accessible and valid for writing
    if not (current_path in requested_path.parents and requested_path.is_file() and requested_path.exists() and os.access(requested_path, os.R_OK | os.W_OK)):
        return make_resp.resp_gen(403) if not current_path in requested_path.parents else make_resp.resp_gen(404)
   
    # Retrieving and processing the request body
    body_len = min(request['body_length'], int(content_length))
    body = request["body"][:body_len].encode()
 
    if requested_path.suffix == '.php':
        resp_body = php_utils.ExecutePHP(requested_path, request, address)
        resp_body_headers = {"content-length": len(resp_body)}
        return make_resp.resp_gen(200, resp_body_headers, resp_body, body_headers=True)
    else:
        try:
            # Writing the request body to the requested file
            with open(requested_path, 'wb') as file:
                file.write(body)
                file.flush()
            return make_resp.resp_gen(200)
        except Exception:
            return make_resp.resp_gen(500)
        

def handle_put_request(request, address):
    requested_path = Path("usr/local/src/web_server/Code/files/" + request["request_uri_path"].strip('/')).resolve()
    current_path = Path("usr/local/src/web_server/Code/files").resolve()

    # Checking if requested path is within the designated directory
    if current_path not in requested_path.parents:
        return make_resp.resp_gen(403)

    content_length = request['headers'].get('Content-Length')

    body_len = min(request['body_length'], int(content_length))
    body = request["body"][:body_len].encode()

    if requested_path.exists():
        try:
            requested_path.write_bytes(body)
            return make_resp.resp_gen(200)
        except Exception:
            return make_resp.resp_gen(500)
    else:
        if not requested_path.parent.exists():
            requested_path.parent.mkdir(parents=True)
        try:
            requested_path.write_bytes(body)
            newfile_location = str(requested_path).replace(str(current_path), '')
            headers = {"Location": newfile_location}
            return make_resp.resp_gen(201, headers, body)
        except Exception:
            return make_resp.resp_gen(500)

def handle_delete_request(request, address):
    requested_path = Path("usr/local/src/web_server/Code/files/" + request["request_uri_path"].strip('/')).resolve()
    current_path = Path("usr/local/src/web_server/Code/files").resolve()

    # Checking if requested path is within the designated directory
    if current_path not in requested_path.parents:
        return make_resp.resp_gen(403)

    # Handling cases when file does not exist
    if not requested_path.exists():
        return make_resp.resp_gen(404)

    # Preventing deletion of Python files
    if str(requested_path).endswith(".py"):
        return make_resp.resp_gen(404)

    try:
        requested_path.unlink()
        return make_resp.resp_gen(200)
    except Exception:
        return make_resp.resp_gen(500)

# Function to handle incoming requests
def handle_request(request, address):
    response = b''
    if request["response"]["code"] != 200:
        response = request["response"]["message"].encode()
    else:
        if request["method"] == "GET":
            response = handle_get_request(request, address)
        elif request["method"] == "POST":
            response = handle_post_request(request, address)
        elif request["method"] == "PUT":
            response = handle_put_request(request, address)
        elif request["method"] == "DELETE":
            response = handle_delete_request(request, address)
        
    return response

# Function to handle incoming data and process requests
def requestHandler(data, address):
    request = parse_req.parse_http(data)
    response = handle_request(request, address)
    return response