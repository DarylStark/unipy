""" Module that contains the UnipyNetwork class. This class
    can be used to use the `network` application """

from typing import Optional
from unipy.unipyconnection import UnipyConnection
from unipy.networkdevice import UnipyNetworkDevice, UnipyNetworkDeviceUSG


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

    def get_devices(self) -> list[UnipyNetworkDevice]:
        """ Method to get all network devices

            Parameters
            ----------
            None

            Returns
            -------
            list[UnipyNetworkDevice]
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
        devices = [self.device_factory(device) for device in data]

        # Return the devicelist
        return devices

    def device_factory(self, data: dict) -> UnipyNetworkDevice:
        """ Method to create a UnipyNetworkDevice object of
            the correct type.

            Parameters
            ----------
            data : dict
                A dictionary with the data to be used to
                create a UnipyNetworkDevice object.

            Returns
            -------
            UnipyNetworkDevice
                The created object
        """
        # Object types
        object_types = {
            'ugw': UnipyNetworkDeviceUSG
        }

        # Find the correct class
        class_object = UnipyNetworkDevice
        if data['type'] in object_types.keys():
            class_object = object_types[data['type']]

        # Create the object
        new_object = class_object(data)

        # Bind this object to this specific UnipyNetwork object
        new_object.bind(self)

        # Return the object
        return new_object
