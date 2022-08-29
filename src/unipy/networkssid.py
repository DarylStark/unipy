""" Module that contains the class for SSIDs """

from typing import Optional
from unipy.unipyapplication import UnipyApplication
from unipy.unipyobject import UnipyObject, ObjectField


class NetworkSSID(UnipyObject):
    """ Dataclass containing all the fields for SSIDs """

    id = ObjectField(type=str, api_field='_id')
    enabled = ObjectField(type=bool, api_field='enabled', default=False)
    name = ObjectField(type=str, api_field='name')
    security = ObjectField(type=str, api_field='security')
    wpa_mode = ObjectField(type=str, api_field='wpa_mode')
    wpa_enc = ObjectField(type=str, api_field='wpa_enc')
    passphrase = ObjectField(type=str, api_field='x_passphrase')

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
