""" Module that contains the baseclass for all objects returned
    from the API """

from dataclasses import dataclass, fields
from logging import getLogger
from typing import Optional
from unipy.unipyapplication import UnipyApplication


@dataclass
class UnipyObject:
    """ Dataclass containing all the methods for objects from
        the API
    """

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
        # Create a logger
        self.logger = getLogger(type(self).__name__)

        self.binding: Optional[UnipyApplication] = binding
        if data:
            self.set_from_dict(data)

    def bind(self, unipynet_object: UnipyApplication) -> None:
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
                        f'Field "{fieldname}" is defined as "{field.type.__name__}", but "{type(data[fieldname]).__name__}" is given in the data')
                    continue
                setattr(self, field.name, data[fieldname])
            else:
                self.logger.error(
                    f'FIELD ERROR: {field.name} defined but not in data')
