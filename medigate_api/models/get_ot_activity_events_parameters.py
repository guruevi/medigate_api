# coding: utf-8

"""
    Medigate API

    # Authentication To use this API, create an API user from Admin Settings > User Management, and generate an API token. Use the token as an [HTTP bearer token](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#authentication_schemes) to authenticate and authorize your API requests.  To use the token, add an `Authorization` header such as: ``` Authorization: Bearer <your token here> ```  # API Conventions  ## Pagination The endpoints in this API are paginated. To iteratively obtain all data, make repeated requests with increasing `offset` starting at 0, and constant `limit`. For example, `{\"offset\": 0, \"limit\": 100}`, followed by `{\"offset\": 100, \"limit\": 100}`, `{\"offset\": 200, \"limit\": 100}`, until less than `limit` results are returned.  ## Filters The endpoints in this API accept a `filter_by` argument to filter the results returned by the endpoint. Filters can be simple filters over a single field, or compound filters made up of other fields. For an example, look at the `filter_by` parameter of the endpoints below.  ### Simple Filters Filters a single field of the result set. The `operation` may be one of:  |`operation`s|Description|`value` Type| |---|---|---| |`in`, `not_in`|Checks for equality/inequality of any of the values|Array of values| |`contains`, `not_contains`|Checks if the string in `value` is contained in the field|string| |`in_subnet`, `not_in_subnet`|Checks if an IP field is in the subnet in `value`|string or list of strings specifying an IP subnet in CIDR notation, such as `\"192.168.1.0/24\"`| | `is_null`, `is_not_null`|Checks if the field has null value|_None_| |`greater`, `greater_or_equal`, `less`, `less_or_equal`|Compares with `value`|a number or timestamp (ISO format) to compare with| |`after_seconds_ago`, `before_seconds_ago`|Compares the field with a timestamp relative to the current date and time|number of seconds|  ### Compound Filters Simple filters can be combined with compound filters. The supported `operation`s are: * `not` - Takes a single filter in `operands`, and negates the filter's condition * `and`, `or` - Take multiple filters in `operands`, and combines them with the appropriate boolean operation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, conint, conlist
from medigate_api.models.filter_by6 import FilterBy6
from medigate_api.models.public_ot_activity_events_fields_enum import PublicOtActivityEventsFieldsEnum
from medigate_api.models.validating_sort_clausepublic_ot_activity_events import ValidatingSortClausepublicOtActivityEvents

class GetOTActivityEventsParameters(BaseModel):
    """
    GetOTActivityEventsParameters
    """
    filter_by: Optional[FilterBy6] = None
    fields: conlist(PublicOtActivityEventsFieldsEnum, min_items=1) = Field(..., description="Specify which fields to return for each item. See the endpoint description for details of supported fields.")
    sort_by: Optional[conlist(ValidatingSortClausepublicOtActivityEvents)] = None
    offset: Optional[StrictInt] = Field(0, description="An offset in the data. This can be used to fetch all data in a paginated manner, by e.g requesting (offset=0, limit=100) followed by (offset=100, limit=100), (offset=200, limit=100), etc.")
    limit: Optional[conint(strict=True, le=5000, ge=0)] = Field(100, description="Maximum amount of items to fetch")
    include_count: Optional[StrictBool] = False
    __properties = ["filter_by", "fields", "sort_by", "offset", "limit", "include_count"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GetOTActivityEventsParameters:
        """Create an instance of GetOTActivityEventsParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of filter_by
        if self.filter_by:
            _dict['filter_by'] = self.filter_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sort_by (list)
        _items = []
        if self.sort_by:
            for _item in self.sort_by:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sort_by'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetOTActivityEventsParameters:
        """Create an instance of GetOTActivityEventsParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetOTActivityEventsParameters.parse_obj(obj)

        _obj = GetOTActivityEventsParameters.parse_obj({
            "filter_by": FilterBy6.from_dict(obj.get("filter_by")) if obj.get("filter_by") is not None else None,
            "fields": obj.get("fields"),
            "sort_by": [ValidatingSortClausepublicOtActivityEvents.from_dict(_item) for _item in obj.get("sort_by")] if obj.get("sort_by") is not None else None,
            "offset": obj.get("offset") if obj.get("offset") is not None else 0,
            "limit": obj.get("limit") if obj.get("limit") is not None else 100,
            "include_count": obj.get("include_count") if obj.get("include_count") is not None else False
        })
        return _obj


