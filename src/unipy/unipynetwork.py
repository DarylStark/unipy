""" Module that contains the UnipyNetwork class. This class
    can be used to use the `network` application """

from typing import Optional
from unipy.networkclient import NetworkActiveClient, NetworkInactiveClient
from unipy.unipyconnection import UnipyConnection
from unipy.networkdevice import NetworkDevice, NetworkDeviceUAP, NetworkDeviceUGW, NetworkDeviceUSW
from unipy.networkportforward import NetworkPortForward
from logging import getLogger


class UnipyNetwork:
    """ Class that can be used to use the `network`
        application """

    def __init__(self, connection: UnipyConnection):
        """ Initiator sets the needed values

            Parameters
            ----------
            connection : UnipyConnection
                A UnipyConnection object that can be used to
                execute API commands.

            Returns
            -------
            None
        """
        self.connection = connection
        self.logger = getLogger(
            f'UnipyNetwork https://{connection.server}/')

    def get_devices(self) -> list[NetworkDevice]:
        """ Method to get all network devices

            Parameters
            ----------
            None

            Returns
            -------
            list[NetworkDevice]
                A list with network devices
        """

        # If not logged in; login
        if self.connection.logged_in:
            self.connection.login()

        # Execute the API request
        resources = self.connection.request(
            method='GET',
            endpoint='proxy/network/api/s/default/stat/device')

        # Get the data and convert it to objects
        data = resources.json()['data']
        resources_converted = [self.device_factory(
            resource) for resource in data]

        # Return the devicelist
        return resources_converted

    def get_active_clients(self) -> list[NetworkActiveClient]:
        """ Method to get all active network clients

            Parameters
            ----------
            None

            Returns
            -------
            list[NetworkActiveClient]
                A list with network devices
        """

        # If not logged in; login
        if self.connection.logged_in:
            self.connection.login()

        # Execute the API request
        resources = self.connection.request(
            method='GET',
            endpoint='proxy/network/v2/api/site/default/clients/active')

        # Get the data and convert it to objects
        data = resources.json()
        resources_converted = [NetworkActiveClient(
            resource) for resource in data]

        # Return the devicelist
        return resources_converted

    def get_inactive_clients(self) -> list[NetworkInactiveClient]:
        """ Method to get all inactive network clients

            Parameters
            ----------
            None

            Returns
            -------
            list[NetworkActiveClient]
                A list with network devices
        """

        # If not logged in; login
        if self.connection.logged_in:
            self.connection.login()

        # Execute the API request
        resources = self.connection.request(
            method='GET',
            endpoint='proxy/network/v2/api/site/default/clients/history?withinHours=0')

        # Get the data and convert it to objects
        data = resources.json()
        resources_converted = [NetworkInactiveClient(
            resource) for resource in data]

        # Return the devicelist
        return resources_converted

    def get_port_forwards(self) -> list[NetworkPortForward]:
        """ Method to get all port forwards

            Parameters
            ----------
            None

            Returns
            -------
            list[UnipyNetworkPortForward]
                A list with network devices
        """

        # If not logged in; login
        if self.connection.logged_in:
            self.connection.login()

        # Execute the API request
        resources = self.connection.request(
            method='GET',
            endpoint='proxy/network/api/s/default/rest/portforward')

        # Get the data and convert it to objects
        data = resources.json()['data']
        resources_converted = [NetworkPortForward(
            resource) for resource in data]

        # Return the devicelist
        return resources_converted

    def device_factory(self, data: dict) -> NetworkDevice:
        """ Method to create a NetworkDevice object of
            the correct type.

            Parameters
            ----------
            data : dict
                A dictionary with the data to be used to
                create a NetworkDevice object.

            Returns
            -------
            NetworkDevice
                The created object
        """
        # Object types
        object_types = {
            'ugw': NetworkDeviceUGW,
            'usw': NetworkDeviceUSW,
            'uap': NetworkDeviceUAP
        }

        # Find the correct class
        class_object = NetworkDevice
        if data['type'] in object_types.keys():
            class_object = object_types[data['type']]
        else:
            self.logger.warning(
                f'No class configured for devicetype "{data["type"]}" in "device_factory"')

        # Create the object
        new_object = class_object(data)

        # Bind this object to this specific UnipyNetwork object
        new_object.bind(self)

        # Return the object
        return new_object
