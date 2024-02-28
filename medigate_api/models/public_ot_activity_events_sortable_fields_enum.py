# coding: utf-8

"""
    Medigate API

    # Authentication To use this API, create an API user from Admin Settings > User Management, and generate an API token. Use the token as an [HTTP bearer token](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#authentication_schemes) to authenticate and authorize your API requests.  To use the token, add an `Authorization` header such as: ``` Authorization: Bearer <your token here> ```  # API Conventions  ## Pagination The endpoints in this API are paginated. To iteratively obtain all data, make repeated requests with increasing `offset` starting at 0, and constant `limit`. For example, `{\"offset\": 0, \"limit\": 100}`, followed by `{\"offset\": 100, \"limit\": 100}`, `{\"offset\": 200, \"limit\": 100}`, until less than `limit` results are returned.  ## Filters The endpoints in this API accept a `filter_by` argument to filter the results returned by the endpoint. Filters can be simple filters over a single field, or compound filters made up of other fields. For an example, look at the `filter_by` parameter of the endpoints below.  ### Simple Filters Filters a single field of the result set. The `operation` may be one of:  |`operation`s|Description|`value` Type| |---|---|---| |`in`, `not_in`|Checks for equality/inequality of any of the values|Array of values| |`contains`, `not_contains`|Checks if the string in `value` is contained in the field|string| |`in_subnet`, `not_in_subnet`|Checks if an IP field is in the subnet in `value`|string or list of strings specifying an IP subnet in CIDR notation, such as `\"192.168.1.0/24\"`| | `is_null`, `is_not_null`|Checks if the field has null value|_None_| |`greater`, `greater_or_equal`, `less`, `less_or_equal`|Compares with `value`|a number or timestamp (ISO format) to compare with| |`after_seconds_ago`, `before_seconds_ago`|Compares the field with a timestamp relative to the current date and time|number of seconds|  ### Compound Filters Simple filters can be combined with compound filters. The supported `operation`s are: * `not` - Takes a single filter in `operands`, and negates the filter's condition * `and`, `or` - Take multiple filters in `operands`, and combines them with the appropriate boolean operation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class PublicOtActivityEventsSortableFieldsEnum(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    DETECTION_TIME = 'detection_time'
    EVENT_TYPE = 'event_type'
    RELATED_ALERT_IDS = 'related_alert_ids'
    DESCRIPTION = 'description'
    DEST_ASSET_ID = 'dest_asset_id'
    DEST_IP = 'dest_ip'
    DEST_DEVICE_TYPE = 'dest_device_type'
    PROTOCOL = 'protocol'
    DEST_PORT = 'dest_port'
    SOURCE_PORT = 'source_port'
    SOURCE_ASSET_ID = 'source_asset_id'
    SOURCE_IP = 'source_ip'
    SOURCE_DEVICE_TYPE = 'source_device_type'
    SOURCE_USERNAME = 'source_username'
    MODE = 'mode'
    EVENT_ID = 'event_id'
    IP_PROTOCOL = 'ip_protocol'

    @classmethod
    def from_json(cls, json_str: str) -> PublicOtActivityEventsSortableFieldsEnum:
        """Create an instance of PublicOtActivityEventsSortableFieldsEnum from a JSON string"""
        return PublicOtActivityEventsSortableFieldsEnum(json.loads(json_str))


