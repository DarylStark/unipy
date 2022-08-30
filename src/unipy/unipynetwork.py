""" Module that contains the UnipyNetwork class. This class
    can be used to use the `network` application """

from typing import Optional
from unipy.exceptions import NoFirewallsFoundError, NoRoutersFoundError
from unipy.networkclient import NetworkActiveClient, NetworkInactiveClient
from unipy.networkfirewall import NetworkFirewallChain, NetworkFirewallGroup, NetworkFirewallRule
from unipy.networksite import NetworkSite
from unipy.networkssid import NetworkSSID
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

    def get_device_system_cfg(self, device_mac: str) -> dict:
        """ Method to get `system` configuration for a device

        Parameters
        ----------
        device_mac : str
            The MAC address of the device

        Returns:
        --------
        dict
            The requested information
        """

        # If not logged in; login
        if self.connection.logged_in:
            self.connection.login()

        # Execute the API request
        resources = self.connection.request(
            method='GET',
            endpoint=f'proxy/network/api/s/default/stat/device/{device_mac}?cfg=system')

        # Get the data and convert it to objects
        data = resources.json()['data'][0]['system_cfg']
        # TODO: Convert to object
        resources_converted = data

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
            list[NetworkInactiveClient]
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

    def get_ssids(self) -> list[NetworkSSID]:
        """ Method to get all SSIDs

            Parameters
            ----------
            None

            Returns
            -------
            list[NetworkSSID]
                A list with network devices
        """

        # If not logged in; login
        if self.connection.logged_in:
            self.connection.login()

        # Execute the API request
        resources = self.connection.request(
            method='GET',
            endpoint='proxy/network/api/s/default/rest/wlanconf')

        # Get the data and convert it to objects
        data = resources.json()['data']
        resources_converted = [NetworkSSID(
            resource) for resource in data]

        # Return the devicelist
        return resources_converted

    def get_firewall_groups(self) -> list[NetworkFirewallGroup]:
        """ Method to get all groups defined for the firewall

            Parameters
            ----------
            None

            Returns
            -------
            list[NetworkFirewallGroup]
                A list with network devices
        """

        # If not logged in; login
        if self.connection.logged_in:
            self.connection.login()

        # Execute the API request
        resources = self.connection.request(
            method='GET',
            endpoint='proxy/network/api/s/default/rest/firewallgroup')

        # Get the data and convert it to objects
        data = resources.json()['data']
        resources_converted = [NetworkFirewallGroup(
            resource) for resource in data]

        # Return the devicelist
        return resources_converted

    def get_firewall_configured_rules(self) -> list[NetworkFirewallRule]:
        """ Method to get all rules defined for the firewall

            Parameters
            ----------
            None

            Returns
            -------
            list[NetworkFirewallRule]
                A list with network devices
        """

        # If not logged in; login
        if self.connection.logged_in:
            self.connection.login()

        # Execute the API request
        resources = self.connection.request(
            method='GET',
            endpoint='proxy/network/api/s/default/rest/firewallrule')

        # Get the data and convert it to objects
        data = resources.json()['data']
        resources_converted = [NetworkFirewallRule(
            resource) for resource in data]

        # Return the devicelist
        return resources_converted

    def get_firewall_rules(self) -> Optional[list]:
        """ Method to get all default rules for the firewall

            Parameters
            ----------
            None

            Returns
            -------
            list[]
                A list with network devices

            None
                No default firewall rules are found
        """
        # If not logged in; login
        if self.connection.logged_in:
            self.connection.login()

        # Get the rules that are configured
        configured = self.get_firewall_configured_rules()
        configured_names = [
            f'{rule.chain}_{rule.chain_index}' for rule in configured]

        # First, we have to find the router for this site
        routers: list[NetworkDeviceUGW] = [
            x for x in self.get_devices() if x.type == 'ugw']

        if len(routers) == 0:
            # No routers found!
            raise NoRoutersFoundError

        # Get the predefined rules for each device
        try:
            firewall_rules = self.get_device_system_cfg(
                device_mac=routers[0].mac_address)['firewall']
            all_rules = firewall_rules['name']
            all_rules.update(firewall_rules['ipv6-name'])
        except (KeyError, IndexError):
            raise NoFirewallsFoundError

        # Loop through the chains and check out the rules
        chains: dict[str, NetworkFirewallChain] = dict()
        for chain, rules in all_rules.items():
            # Create a chain object
            chain_object = NetworkFirewallChain(rules)
            chain_object.name = chain
            if 'rule' in rules.keys():
                chain_object.rules = list()
                for rule, details in rules['rule'].items():
                    if f'{chain}_{rule}' not in configured_names:
                        # Not a configured rule, create a
                        # NetworkFirewallRule for it.
                        rule_object = NetworkFirewallRule()
                        rule_object.name = details['description']
                        rule_object.enabled = True
                        rule_object.chain = chain
                        rule_object.chain_index = int(rule)
                        rule_object.action = details['action']
                        rule_object.is_predefined = True
                        chain_object.rules.append(rule_object)

            # Add the chain to the chains list
            chains[chain] = chain_object

        # Add the configured rules
        for configured_rule in configured:
            if chains[configured_rule.chain].rules is None:
                chains[configured_rule.chain].rules = list()
            chains[configured_rule.chain].rules.append(configured_rule)

        # Sort the rules
        for chain, chain_object in chains.items():
            if chain_object.rules:
                chain_object.rules.sort(key=lambda rule: rule.chain_index)

        return chains

    def get_sites(self) -> list[NetworkSite]:
        """ Method to get all sites

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
            endpoint='proxy/network/api/self/sites')

        # Get the data and convert it to objects
        data = resources.json()['data']
        resources_converted = [NetworkSite(
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
