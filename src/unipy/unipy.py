""" Module that contains the Unipy class """

from unipy.unipyconnection import UnipyConnection
from unipy.unipynetwork import UnipyNetwork


class Unipy:
    """ The Unipy class can be used to connect to a UnifyOS
        device and interact with the applications. This class
        does not have to be used to use the specific methods
        for applications, but uses composition to make it
        easier. """

    def __init__(self,
                 server: str,
                 username: str,
                 password: str,
                 verify: bool = True) -> None:
        """ Initiator sets default values

            Parameters
            ----------
            server : str
                The Unifi server to connect to

            username : str
                The username to connect with

            password : str
                The password to connect with

            verify : bool = False
                If True, the UnifiOS certificate will be verified

            Returns
            -------
            None
        """

        # Create the connection object
        self.connection = UnipyConnection(
            server=server,
            username=username,
            password=password,
            verify=verify)

        # Add objects for the applications
        self.network = UnipyNetwork(self.connection)

    def login(self) -> None:
        """ Method to login to Unifi. Uses the UnipyConnection
            object.

            Parameters
            ----------
            None

            Returns
            -------
            None
        """
        return self.connection.login()

    def logout(self) -> None:
        """ Method to logout from to Unifi. Uses the
            UnipyConnection object.

            Parameters
            ----------
            None

            Returns
            -------
            None
        """
        return self.connection.logout()
