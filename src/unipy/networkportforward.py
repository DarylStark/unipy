""" Module that contains the class for Port Forwards """
from typing import Optional
from unipy.unipyapplication import UnipyApplication
from unipy.unipyobject import UnipyObject, ObjectField


class NetworkPortForward(UnipyObject):
    """ Dataclass containing all the fields for port forwards """

    id = ObjectField(type=str, api_field='_id')
    enabled = ObjectField(type=bool, api_field='enabled', default=False)
    name = ObjectField(type=str, api_field='name')
    dst_port = ObjectField(type=int, api_field='dst_port', default=0)
    fwd_port = ObjectField(type=int, api_field='fwd_port', default=0)
    fwd = ObjectField(type=str, api_field='fwd', default=0)
    log = ObjectField(type=bool, api_field='log', default=False)
    src = ObjectField(type=str, api_field='src')
    proto = ObjectField(type=str, api_field='proto')
    site_id = ObjectField(type=str, api_field='site_id')
    pfwd_interface = ObjectField(type=str, api_field='pfwd_interface')
    destination_ip = ObjectField(type=str, api_field='destination_ip')

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
