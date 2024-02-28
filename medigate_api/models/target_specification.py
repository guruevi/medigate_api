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

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from medigate_api.models.public_alert_target_spec import PublicAlertTargetSpec
from medigate_api.models.public_device_target_spec import PublicDeviceTargetSpec
from medigate_api.models.public_vulnerability_target_spec import PublicVulnerabilityTargetSpec
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

TARGETSPECIFICATION_ONE_OF_SCHEMAS = ["PublicAlertTargetSpec", "PublicDeviceTargetSpec", "PublicVulnerabilityTargetSpec"]

class TargetSpecification(BaseModel):
    """
    TargetSpecification
    """
    # data type: PublicDeviceTargetSpec
    oneof_schema_1_validator: Optional[PublicDeviceTargetSpec] = None
    # data type: PublicAlertTargetSpec
    oneof_schema_2_validator: Optional[PublicAlertTargetSpec] = None
    # data type: PublicVulnerabilityTargetSpec
    oneof_schema_3_validator: Optional[PublicVulnerabilityTargetSpec] = None
    if TYPE_CHECKING:
        actual_instance: Union[PublicAlertTargetSpec, PublicDeviceTargetSpec, PublicVulnerabilityTargetSpec]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(TARGETSPECIFICATION_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

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
    def actual_instance_must_validate_oneof(cls, v):
        instance = TargetSpecification.construct()
        error_messages = []
        match = 0
        # validate data type: PublicDeviceTargetSpec
        if not isinstance(v, PublicDeviceTargetSpec):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PublicDeviceTargetSpec`")
        else:
            match += 1
        # validate data type: PublicAlertTargetSpec
        if not isinstance(v, PublicAlertTargetSpec):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PublicAlertTargetSpec`")
        else:
            match += 1
        # validate data type: PublicVulnerabilityTargetSpec
        if not isinstance(v, PublicVulnerabilityTargetSpec):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PublicVulnerabilityTargetSpec`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TargetSpecification with oneOf schemas: PublicAlertTargetSpec, PublicDeviceTargetSpec, PublicVulnerabilityTargetSpec. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TargetSpecification with oneOf schemas: PublicAlertTargetSpec, PublicDeviceTargetSpec, PublicVulnerabilityTargetSpec. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> TargetSpecification:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> TargetSpecification:
        """Returns the object represented by the json string"""
        instance = TargetSpecification.construct()
        error_messages = []
        match = 0

        # deserialize data into PublicDeviceTargetSpec
        try:
            instance.actual_instance = PublicDeviceTargetSpec.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PublicAlertTargetSpec
        try:
            instance.actual_instance = PublicAlertTargetSpec.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PublicVulnerabilityTargetSpec
        try:
            instance.actual_instance = PublicVulnerabilityTargetSpec.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TargetSpecification with oneOf schemas: PublicAlertTargetSpec, PublicDeviceTargetSpec, PublicVulnerabilityTargetSpec. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TargetSpecification with oneOf schemas: PublicAlertTargetSpec, PublicDeviceTargetSpec, PublicVulnerabilityTargetSpec. Details: " + ", ".join(error_messages))
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
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


