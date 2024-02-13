def get_resp_message(code):
    if code == 200:
        return "HTTP/1.1 200 OK\r\n"
    elif code == 201:
        return "HTTP/1.1 201 Created\r\n"
    elif code == 400:
        return "HTTP/1.1 400 Bad Request\r\n"
    elif code == 403:
        return "HTTP/1.1 403 Forbidden\r\n"
    elif code == 404:
        return "HTTP/1.1 404 Not Found\r\n"
    elif code == 405:
        return "HTTP/1.1 405 Not Implemented\r\n"
    elif code == 411:
        return "HTTP/1.1 411 Length Required\r\n"
    elif code == 500:
        return "HTTP/1.1 500 Internal Server Error\r\n"
    elif code == 501:
        return "HTTP/1.1 501 Not Implemented\r\n"
    elif code == 505:
        return "HTTP/1.1 505 HTTP Version Not Supported\r\n"
    else:
        return "HTTP/1.1 {} Unknown\r\n".format(code)

def header_gen(headers):
    resp = ""
    for name in headers.keys():
        resp += "{}: {}\r\n".format(name, headers[name])
    return resp


def resp_gen(code, headers=None, body=None, body_headers=False):
    resp = get_resp_message(code)
    if headers:
        resp += header_gen(headers) 
    else:
        resp += "\r\n"    
    resp = resp.encode('ascii')

    if body:
        if not body_headers:
            resp += b"\r\n"
        resp += body
    return resp
