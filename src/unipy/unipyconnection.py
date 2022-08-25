""" Module that contains the class to connect to Unifi """

from requests import Request, Response, Session
from requests.exceptions import Timeout, ConnectionError
import urllib3
from typing import Optional
from unipy.exceptions import PermissionDeniedError
from logging import getLogger


class UnipyConnection:
    """ Class that can be used to create a connection to a
        UnifiOS device """

    def __init__(self,
                 server: str,
                 username: str,
                 password: str,
                 verify: bool = True) -> None:
        """ The initiator sets the values for the object

            Parameters
            ----------
            username : str
                The username of the UnifiOS device

            password : str
                The password of the UnifiOS device

            server : str
                The servername or IP address of the UnifiOS device

            verify : bool = False
                If True, the UnifiOS certificate will be verified

            Returns
            -------
            None
        """
        # Create a logger
        self.logger = getLogger(
            f'UnipyConnection_{username}@{server}')

        # Set the default values
        self.username = username
        self.password = password
        self.server = server
        self.verify = verify

        # Create a requests session object. This can e used to
        # execute API requests and keep the given headers
        self.session = Session()
        self.session.verify = verify

        # Disable warning about unverified HTTPs certificates
        if not verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Not logged in yet
        self.logged_in = False

    def request(self,
                method: str,
                endpoint: str,
                data: Optional[dict] = None) -> Response:
        """ Method to execute a API request

            Parameters
            ----------
            method : str
                The HTTP method to use

            endpoint : str
                The endpoint to execute

            data : dict = None
                The data to send to the API

            Returns
            -------
            Response
                The response object from the requests library
        """

        # Compile the URL
        url = f'https://{self.server}/{endpoint}'
        request = Request(
            method=method,
            url=url,
            json=data)

        # Prepare the request
        prep = self.session.prepare_request(request)
        try:
            api_request = self.session.send(prep)
        except (Timeout, ConnectionError):
            self.logger.error(
                f'Unable to connect to Unifi server "{self.server}"')
            # TODO: Raise correct exception
            raise PermissionDeniedError()

        if api_request.status_code == 403:
            raise PermissionDeniedError(
                f'Received a error 403 from Unifi for url {url}')

        return api_request

    def login(self) -> None:
        """ Method to login to Unifi

            Parameters
            ----------
            None

            Returns
            -------
            None
        """

        try:
            login = self.request(
                method='POST',
                endpoint='api/auth/login',
                data={
                    'username': self.username,
                    'password': self.password
                }
            )

            # Set the X-CSRF-Token header; this is needed for
            # some endpoints
            self.session.headers.update(
                {'X-CSRF-Token': login.headers['X-CSRF-Token']})
        except PermissionDeniedError:
            # Failed; remove everything
            if 'X-CSRF-Token' in self.session.headers.keys():
                self.session.headers.pop('X-CSRF-Token', None)
            self.logged_in = False

            # TODO: Raise exception
        else:
            # Logged in!
            self.logged_in = True

    def logout(self) -> None:
        """ Method to logout from Unifi

            Members
            -------
            None
        """
        if self.logged_in:
            login = self.request(
                method='POST',
                endpoint='api/auth/logout'
            )
            self.session.headers.pop('X-CSRF-Token')
            self.logged_in = False
