""" Module that contains the baseclass for all objects returned
    from the API """

from dataclasses import dataclass, fields
from logging import getLogger
from typing import Optional, Any
from unipy.unipyapplication import UnipyApplication


@dataclass
class ObjectField:
    type: type
    api_field: str
    default: Any = None


class UnipyObject:
    """ Dataclass containing all the methods for objects from
        the API
    """

    __model = dict()

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

        # Set the binding
        self.binding: Optional[UnipyApplication] = binding

        # Empty dict with API fields
        self.api_fields = dict()

        # Loop through all fields in the model, add it to the
        # API cache and set the attribute with either the
        # configured default value, or the default value for
        # the configured object type
        for field in dir(self.__class__):
            attr = getattr(self, field)
            if type(attr) is ObjectField:
                self.api_fields[attr.api_field] = field
                self.__model[field] = attr
                if attr.default:
                    setattr(self, field, attr.default)
                else:
                    setattr(self, field, attr.type())

        if data:
            self.set_from_api(data)

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

    def set_from_api(self, data: dict) -> None:
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
        for field, value in data.items():
            if field in self.api_fields:
                field_name = self.api_fields[field]
                field_type = self.__model[field_name].type
                if type(value) is not field_type:
                    try:
                        value = field_type(value)
                    except ValueError as error:
                        self.logger.warning(
                            f'Field "{field_name}" should be of type "{field_type.__name__}" but API gives "{type(value).__name__}". Converting failed!')
                        self.logger.debug(f'Error: {error}')
                setattr(self, field_name, value)
