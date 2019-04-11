""" Module with project custom exceptions."""


class SystemFileReadError(IOError):
    """ Exception which can be raised if system file from /proc directory
        can not be read.
    """
    pass
