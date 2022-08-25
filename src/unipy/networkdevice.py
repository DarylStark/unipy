""" Module that contains dataclasses for network devices """

import requests
import urllib3
from typing import Optional
from dataclasses import dataclass, fields
from logging import getLogger


@dataclass
class UnipyNetworkDevice:
    """ Dataclass containing all the fields for network devices

        Members
        -------
        Too much to describe
    """
    _id: str = None
    ip: str = None
    mac: str = None
    model: str = None
    type: str = None
    version: str = None
    adopted: bool = None
    site_id: str = None
    cfgversion: str = None
    config_network: str = None
    license_state: str = None
    inform_url: str = None
    inform_ip: str = None
    hw_caps: int = None
    fw_caps: int = None
    serial: str = None
    name: str = None
    model_incompatible: bool = None
    model_in_lts: bool = None
    model_in_eol: bool = None
    snmp_contact: str = None
    snmp_location: str = None
    connected_at: int = None
    provisioned_at: int = None
    device_id: str = None
    uplink: str = None
    state: int = None
    last_seen: int = None
    upgradable: bool = None
    known_cfgversion: str = None
    uptime: int = None
    connect_request_ip: str = None
    connect_request_port: str = None
    startup_timestamp: int = None
    tx_bytes: int = None
    rx_bytes: int = None
    x_has_ssh_hostkey: bool = None

    def __init__(self, data: Optional[dict] = None) -> None:
        """ Sets the values

            Parameters
            ----------
            data : Optional[dict]
                If given, this data is used to fill the
                object

            Returns
            -------
            None
        """
        # Create a logger
        self.logger = getLogger(f'UnipyNetworkDevice')

        self.binding = None
        if data:
            self.set_from_dict(data)

    def bind(self, unipynet_object: 'UnipyNetwork') -> None:
        """ Method to bind this object to a UnipyNetwork
            object.

            Parameters
            ----------
            unipynet_object : UnipyNetwork
                The UnipyNetwork object to bind

            Returns
            -------
            None
        """
        self.binding = unipynet_object

    def set_from_dict(self, data: dict) -> None:
        """ Method to set the values from a dict that comes
            from the API.

            Parameters
            ----------
            data : Optional[dict]
                Data used to fill the object

            Returns
            -------
            None

            Parameters
            ----------
            Parameters and their types

            Returns
            -------
            Return values
        """

        # Loop through the fields of this object and set them
        # if given in the data
        for field in fields(self):
            fieldname = field.name
            possible_fields = [
                field.name,
                field.name.replace('_', '-')
            ]
            for possible_field in possible_fields:
                if possible_field in data.keys():
                    fieldname = possible_field
                    break

            if fieldname in data.keys():
                if type(data[fieldname]) is not field.type:
                    self.logger.warning(
                        f'FIELD ERROR: {fieldname} should be {field.type}, is {type(data[fieldname])}')
                    continue
                setattr(self, field.name, data[fieldname])
            else:
                self.logger.error(
                    f'FIELD ERROR: {field.name} defined but not in data')


@dataclass
class UnipyNetworkDeviceUSG(UnipyNetworkDevice):
    """ Dataclass for a USG device

        Members
        -------
        speedtest_status_saved : bool
            Determines if the status of the speedtest is
            saved
    """
    speedtest_status_saved: bool = None

    def __init__(self, data: Optional[dict] = None) -> None:
        super().__init__(data)
