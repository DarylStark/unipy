""" Module that contains dataclasses for network clients """

from typing import Optional
from unipy.unipyapplication import UnipyApplication
from unipy.unipyobject import UnipyObject, ObjectField


class NetworkClient(UnipyObject):
    """ Dataclass containing all the fields for network
        clients """

    id = ObjectField(type=str, api_field='id')
    hostname = ObjectField(type=str, api_field='hostname')
    display_name = ObjectField(type=str, api_field='display_name')
    blocked = ObjectField(type=bool, api_field='blocked')
    first_seen = ObjectField(type=int, api_field='first_seen')
    last_seen = ObjectField(type=int, api_field='last_seen')
    ipv4_address = ObjectField(type=str, api_field='ip')
    fixed_ipv4_address = ObjectField(type=str, api_field='fixed_ip')
    mac_address = ObjectField(type=str, api_field='mac')
    status = ObjectField(type=str, api_field='status')
    type = ObjectField(type=str, api_field='type')
    unifi_device = ObjectField(type=bool, api_field='unifi_device')
    fixed_ip = ObjectField(type=bool, api_field='use_fixedip')
    wired = ObjectField(type=bool, api_field='is_wired')

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


class NetworkActiveClient(NetworkClient):
    """ Dataclass containing all the fields for active
        network clients """

    uptime = ObjectField(type=int, api_field='uptime')

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


class NetworkInactiveClient(NetworkClient):
    """ Dataclass containing all the fields for inactive
        network clients """

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
