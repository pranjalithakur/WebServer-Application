import re
from exception import *
import logging

logger = logging.getLogger(__name__)

ALLOWED_SCHEMES = ['http', 'https']

URI_REGEX = re.compile(r"^(([^:\/\/?#]+):)?(\/\/([^\/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?")

def parse_request_uri(uri, request):
    uri_match = URI_REGEX.match(uri)

    scheme = uri_match.group(2)
    authority = uri_match.group(4)
    path = uri_match.group(5)
    query = uri_match.group(7)
    fragment = uri_match.group(9)

    if scheme:
        if scheme not in ALLOWED_SCHEMES:
            raise HTTPRequestParseError
        request["request_uri_scheme"] = scheme

    if authority:
        request["request_uri_authority"] = authority

    if path:
        request["request_uri_path"] = path

    if query:
        request["request_uri_query"] = query

    if fragment:
        request["request_uri_fragment"] = fragment

    return


def parse_request_line(request_line, request):
    request_line_data = request_line.split()

    if len(request_line_data) != 3: 
          raise HTTPRequestParseError
    
    request['method'] = request_line_data[0]
    parse_request_uri(request_line_data[1], request)
    request['http_version'] = request_line_data[2]
    
    return


def parse_request_header(header, request):
    header_data = header.split(':', 1) 
    if len(header_data) != 2:
        raise HTTPRequestParseError
    request['headers'][header_data[0]] = header_data[1]

    return


def parse_http_header(header, request):
    lines = header.split('\r\n')
    parse_request_line(lines[0], request)
    for line in lines[1:]:
        if line:
            parse_request_header(line, request)

    return


def parse_http(http_request):
    header, body = http_request.split('\r\n\r\n', 1)
    request = {'headers': {}, 'body': body, "response":{}, "body_length" : len(body)}
    try:
        parse_http_header(header, request)
        request["response"]["code"] = 200
        request["response"]["message"] = "HTTP/1.1 200 OK\r\n"

    except HTTPRequestParseError as e:
        request["response"]["code"] = 400
        request["response"]["message"] = "HTTP/1.1 400 Bad Request\r\n\r\n"
	
    except HTTPRequestMethodNotAllowed as e:
        request["response"]["code"] = 405
        request["response"]["message"] = "HTTP/1.1 405 Method Not Allowed\r\n\r\n"
	
    except HTTPRequestMethodUnknown as e:
        request["response"]["code"] = 501
        request["response"]["message"] = "HTTP/1.1 501 Not Implemented\r\n\r\n"
        
    except HTTPVersionNotSupported as e:
        request["response"]["code"] = 505
        request["response"]["message"] = "HTTP/1.1 505 HTTP Version Not Supported\r\n\r\n"
        
    except (HTTPServerError, Exception) as e:
        request["response"]["code"] = 500
        request["response"]["message"] = "HTTP/1.1 500 Internal Server Error\r\n\r\n"

    return request