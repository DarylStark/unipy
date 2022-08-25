""" Module that contains the class for Port Forwards """
from dataclasses import dataclass
from typing import Optional
from unipy.unipyapplication import UnipyApplication
from unipy.unipyobject import UnipyObject


@dataclass
class NetworkPortForward(UnipyObject):
    """ Dataclass containing all the fields for port forwards

        Members
        -------
        Too much to describe
    """
    _id: str = None
    enabled: bool = False
    name: str = None
    dst_port: str = None    # Should be int
    fwd_port: str = None    # Should be int
    fwd: str = None
    log: bool = False
    src: str = None
    proto: str = None
    site_id: str = None
    pfwd_interface: str = None
    destination_ip: str = None

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
