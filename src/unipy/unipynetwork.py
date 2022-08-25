""" Module that contains the UnipyNetwork class. This class
    can be used to use the `network` application """

from typing import Optional
from unipy.unipyconnection import UnipyConnection
from unipy.networkdevice import NetworkDevice, NetworkDeviceUSG
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
            'ugw': NetworkDeviceUSG
        }

        # Find the correct class
        class_object = NetworkDevice
        if data['type'] in object_types.keys():
            class_object = object_types[data['type']]
        else:
            self.logger.warning(
                f'No class configured for devicetype "{data["type"]}"')

        # Create the object
        new_object = class_object(data)

        # Bind this object to this specific UnipyNetwork object
        new_object.bind(self)

        # Return the object
        return new_object
