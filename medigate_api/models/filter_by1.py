# coding: utf-8

"""
    Medigate API

    # Authentication To use this API, create an API user from Admin Settings > User Management, and generate an API token. Use the token as an [HTTP bearer token](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#authentication_schemes) to authenticate and authorize your API requests.  To use the token, add an `Authorization` header such as: ``` Authorization: Bearer <your token here> ```  # API Conventions  ## Pagination The endpoints in this API are paginated. To iteratively obtain all data, make repeated requests with increasing `offset` starting at 0, and constant `limit`. For example, `{\"offset\": 0, \"limit\": 100}`, followed by `{\"offset\": 100, \"limit\": 100}`, `{\"offset\": 200, \"limit\": 100}`, until less than `limit` results are returned.  ## Filters The endpoints in this API accept a `filter_by` argument to filter the results returned by the endpoint. Filters can be simple filters over a single field, or compound filters made up of other fields. For an example, look at the `filter_by` parameter of the endpoints below.  ### Simple Filters Filters a single field of the result set. The `operation` may be one of:  |`operation`s|Description|`value` Type| |---|---|---| |`in`, `not_in`|Checks for equality/inequality of any of the values|Array of values| |`contains`, `not_contains`|Checks if the string in `value` is contained in the field|string| |`in_subnet`, `not_in_subnet`|Checks if an IP field is in the subnet in `value`|string or list of strings specifying an IP subnet in CIDR notation, such as `\"192.168.1.0/24\"`| | `is_null`, `is_not_null`|Checks if the field has null value|_None_| |`greater`, `greater_or_equal`, `less`, `less_or_equal`|Compares with `value`|a number or timestamp (ISO format) to compare with| |`after_seconds_ago`, `before_seconds_ago`|Compares the field with a timestamp relative to the current date and time|number of seconds|  ### Compound Filters Simple filters can be combined with compound filters. The supported `operation`s are: * `not` - Takes a single filter in `operands`, and negates the filter's condition * `and`, `or` - Take multiple filters in `operands`, and combines them with the appropriate boolean operation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from medigate_api.models.validating_compound_query_filter_alerted_device import ValidatingCompoundQueryFilterAlertedDevice
from medigate_api.models.validating_simple_query_filter_alerted_device import ValidatingSimpleQueryFilterAlertedDevice
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

FILTERBY1_ANY_OF_SCHEMAS = ["ValidatingCompoundQueryFilterAlertedDevice", "ValidatingSimpleQueryFilterAlertedDevice"]

class FilterBy1(BaseModel):
    """
    Filters which devices are returned. Can be a simple filter on a single field, or a combination of several filters for more complex logic.
    """

    # data type: ValidatingSimpleQueryFilterAlertedDevice
    anyof_schema_1_validator: Optional[ValidatingSimpleQueryFilterAlertedDevice] = None
    # data type: ValidatingCompoundQueryFilterAlertedDevice
    anyof_schema_2_validator: Optional[ValidatingCompoundQueryFilterAlertedDevice] = None
    if TYPE_CHECKING:
        actual_instance: Union[ValidatingCompoundQueryFilterAlertedDevice, ValidatingSimpleQueryFilterAlertedDevice]
    else:
        actual_instance: Any
    any_of_schemas: List[str] = Field(FILTERBY1_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = FilterBy1.construct()
        error_messages = []
        # validate data type: ValidatingSimpleQueryFilterAlertedDevice
        if not isinstance(v, ValidatingSimpleQueryFilterAlertedDevice):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValidatingSimpleQueryFilterAlertedDevice`")
        else:
            return v

        # validate data type: ValidatingCompoundQueryFilterAlertedDevice
        if not isinstance(v, ValidatingCompoundQueryFilterAlertedDevice):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValidatingCompoundQueryFilterAlertedDevice`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in FilterBy1 with anyOf schemas: ValidatingCompoundQueryFilterAlertedDevice, ValidatingSimpleQueryFilterAlertedDevice. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> FilterBy1:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> FilterBy1:
        """Returns the object represented by the json string"""
        instance = FilterBy1.construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[ValidatingSimpleQueryFilterAlertedDevice] = None
        try:
            instance.actual_instance = ValidatingSimpleQueryFilterAlertedDevice.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[ValidatingCompoundQueryFilterAlertedDevice] = None
        try:
            instance.actual_instance = ValidatingCompoundQueryFilterAlertedDevice.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FilterBy1 with anyOf schemas: ValidatingCompoundQueryFilterAlertedDevice, ValidatingSimpleQueryFilterAlertedDevice. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

