""" Module that contains dataclasses for network devices """

import requests
import urllib3
from typing import Optional
from dataclasses import dataclass, fields
from logging import getLogger
from unipy.unipyapplication import UnipyApplication
from unipy.unipyobject import UnipyObject, ObjectField


@dataclass
class NetworkDevice(UnipyObject):
    """ Dataclass containing all the fields for network devices

        Members
        -------
        Too much to describe
    """
    id = ObjectField(type=str, api_field='_id')
    ipv4_address = ObjectField(type=str, api_field='ip')
    mac_address = ObjectField(type=str, api_field='mac')
    model = ObjectField(type=str, api_field='model')
    type = ObjectField(type=str, api_field='type')
    version = ObjectField(type=str, api_field='version')
    adopted = ObjectField(type=bool, api_field='adopted')
    site_id = ObjectField(type=str, api_field='site_id')
    cfg_version = ObjectField(type=str, api_field='cfgversion')
    cfg_network = ObjectField(type=str, api_field='config_network')
    license_state = ObjectField(type=str, api_field='license_state')
    inform_url = ObjectField(type=str, api_field='inform_url')
    inform_ip = ObjectField(type=str, api_field='inform_ip')
    hw_caps = ObjectField(type=int, api_field='hw_caps')
    fw_caps = ObjectField(type=int, api_field='fw_caps')
    serial = ObjectField(type=str, api_field='serial')
    name = ObjectField(type=str, api_field='name')
    model_incompatible = ObjectField(type=bool, api_field='model_incompatible')
    model_in_lts = ObjectField(type=bool, api_field='model_in_lts')
    model_in_eol = ObjectField(type=bool, api_field='model_in_eol')
    snmp_contact = ObjectField(type=str, api_field='snmp_contact')
    snmp_location = ObjectField(type=str, api_field='snmp_location')
    connected_at = ObjectField(type=int, api_field='connected_at')
    provisioned_at = ObjectField(type=int, api_field='provisioned_at')
    device_id = ObjectField(type=str, api_field='device_id')
    uplink = ObjectField(type=str, api_field='uplink')
    state = ObjectField(type=int, api_field='state')
    last_seen = ObjectField(type=int, api_field='last_seen')
    upgradable = ObjectField(type=bool, api_field='upgradable')
    known_cfgversion = ObjectField(type=str, api_field='known_cfgversion')
    uptime = ObjectField(type=int, api_field='uptime')
    connect_request_ip = ObjectField(type=str, api_field='uptime')
    connect_request_port = ObjectField(type=int, api_field='uptime')
    startup_timestamp = ObjectField(type=int, api_field='startup_timestamp')
    tx_bytes = ObjectField(type=int, api_field='tx_bytes')
    rx_bytes = ObjectField(type=int, api_field='rx_bytes')
    x_has_ssh_hostkey = ObjectField(type=bool, api_field='x_has_ssh_hostkey')

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
    speedtest_status_saved = ObjectField(
        type=bool, api_field='speedtest_status')

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
