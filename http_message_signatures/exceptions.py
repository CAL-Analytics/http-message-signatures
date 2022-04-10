class HTTPMessageSignaturesException(Exception):
    "Base class for exceptions raised by http_message_signatures"


class InvalidSignature(Exception):
    "Class for exceptions raised in the course of verifying an HTTP message signature"
