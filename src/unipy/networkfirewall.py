""" Module that contains the class for firewall objects """

from typing import Optional
from unipy.unipyapplication import UnipyApplication
from unipy.unipyobject import UnipyObject, ObjectField


class NetworkFirewallGroup(UnipyObject):
    """ Dataclass containing all the fields for firewall groups """

    id = ObjectField(type=str, api_field='_id')
    name = ObjectField(type=str, api_field='name')
    group_type = ObjectField(type=str, api_field='group_type')
    members = ObjectField(type=list, api_field='group_members')

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


class NetworkFirewallChain(UnipyObject):
    """ Class that represents a chain for the network firewall """

    name = ObjectField(type=str)
    default_action = ObjectField(type=str, api_field='default-action')
    description = ObjectField(type=str, api_field='description')
    rules = ObjectField(type=list, default=None)

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


class NetworkFirewallRule(UnipyObject):
    """ Dataclass containing all the fields for firewall
        rules """

    is_predefined = ObjectField(type=bool, default=False)
    id = ObjectField(type=str, api_field='_id', default=None)
    name = ObjectField(type=str, api_field='name')
    enabled = ObjectField(type=bool, api_field='enabled')
    dst_firewall_group_ids = ObjectField(
        type=list, api_field='dst_firewallgroup_ids', default=None)
    src_firewall_group_ids = ObjectField(
        type=list, api_field='src_firewallgroup_ids', default=None)
    chain = ObjectField(type=str, api_field='ruleset')
    chain_index = ObjectField(type=int, api_field='rule_index')
    logging = ObjectField(type=bool, api_field='logging', default=False)
    action = ObjectField(type=str, api_field='action')

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
