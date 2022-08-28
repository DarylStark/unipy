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

    object_model = dict()

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

        # Inherit the fields
        self.set_fields()

        # Set the binding
        self.binding: Optional[UnipyApplication] = binding

        # Empty dict with API fields
        self.api_fields = dict()

        # Loop through all fields in the model, set the
        # default value and add it to the API cache
        for field, model in self.object_model.items():
            self.api_fields[model.api_field] = field
            if model.default:
                setattr(self, field, model.default)
            else:
                setattr(self, field, model.type())

        if data:
            self.set_from_api(data)

    def set_fields(self) -> None:
        """ Method that makes sure the model is inherited
            from base classes

            Parameters
            ----------
            None

            Returns
            -------
            None
        """
        # Get the path till we reach the last base class
        base_path = list()
        current_base = self.__class__
        while current_base is not object:
            bases = current_base.__bases__
            if bases[0] is not object:
                base_path.insert(0, bases[0])
            current_base = bases[0]

        # Merge all models
        new_model = base_path[0].object_model
        for base in base_path[1:]:
            new_model.update(base.object_model)
        new_model.update(self.object_model)
        self.object_model = new_model

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
                field_type = self.object_model[field_name].type
                if type(value) is not field_type:
                    value = field_type(value)
                else:
                    print(type(value))
                setattr(self, field_name, value)
