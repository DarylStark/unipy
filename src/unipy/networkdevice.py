""" Module that contains dataclasses for network devices """

import requests
import urllib3
from typing import Optional
from dataclasses import dataclass, fields
from logging import getLogger
from unipy.unipyapplication import UnipyApplication
from unipy.unipyobject import UnipyObject


@dataclass
class NetworkDevice(UnipyObject):
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

    def __init__(self,
                 data: Optional[dict] = None,
                 binding: Optional[UnipyApplication] = None) -> None:
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
        super().__init__(data, binding)


@dataclass
class NetworkDeviceUSG(NetworkDevice):
    """ Dataclass for a USG device

        Members
        -------
        speedtest_status_saved : bool
            Determines if the status of the speedtest is
            saved
    """
    speedtest_status_saved: bool = None

    def __init__(self,
                 data: Optional[dict] = None,
                 binding: Optional[UnipyApplication] = None) -> None:
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
        super().__init__(data, binding)
