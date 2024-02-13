class HTTPRequestParseError(Exception):
    """400 BAD REQUEST"""

class HTTPNotFound(Exception):
	"""404 NOT FOUND"""

class HTTPRequestMethodNotAllowed(Exception):
	"""405 METHOD NOT ALLOWED."""
	
class HTTPServerError(Exception):
	"""500 INTERNAL SERVER ERROR"""

class HTTPRequestMethodUnknown(Exception):
	"""501 NOT IMPLEMENTED."""

class HTTPVersionNotSupported(Exception):
	"""505 HTTP VERSION NOT SUPPORTED"""