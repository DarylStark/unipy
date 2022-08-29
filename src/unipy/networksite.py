""" Module that contains the class for Sites """

from typing import Optional
from unipy.unipyapplication import UnipyApplication
from unipy.unipyobject import UnipyObject, ObjectField


class NetworkSite(UnipyObject):
    """ Dataclass containing all the fields for sites """

    id = ObjectField(type=str, api_field='_id')
    anonymous_id = ObjectField(type=str, api_field='anonymous_id')
    name = ObjectField(type=str, api_field='name')
    description = ObjectField(type=str, api_field='desc')
    role = ObjectField(type=str, api_field='role')
    hidden_id = ObjectField(type=str, api_field='attr_hidden_id')

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
