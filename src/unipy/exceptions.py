""" Module that contains all the exceptions for the library """


class PermissionDeniedError(Exception):
    """ Error when a API request is denied """
    pass


class NoRoutersFoundError(Exception):
    """ Error when the library is searching for a router but
        can't find any """
    pass


class NoFirewallsFoundError(Exception):
    """ Error when the library is searching for a firewall but
        can't find any """
    pass
