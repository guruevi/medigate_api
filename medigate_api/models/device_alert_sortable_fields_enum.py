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





class DeviceAlertSortableFieldsEnum(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    DEVICE_UID = 'device_uid'
    DEVICE_NAME = 'device_name'
    DEVICE_IP_LIST = 'device_ip_list'
    DEVICE_MAC_LIST = 'device_mac_list'
    DEVICE_NETWORK_LIST = 'device_network_list'
    DEVICE_CATEGORY = 'device_category'
    DEVICE_SUBCATEGORY = 'device_subcategory'
    DEVICE_TYPE = 'device_type'
    DEVICE_RETIRED = 'device_retired'
    DEVICE_ASSIGNEES = 'device_assignees'
    DEVICE_LABELS = 'device_labels'
    DEVICE_PURDUE_LEVEL = 'device_purdue_level'
    DEVICE_SITE_NAME = 'device_site_name'
    DEVICE_FIRST_SEEN_LIST = 'device_first_seen_list'
    DEVICE_LAST_SEEN_LIST = 'device_last_seen_list'
    DEVICE_RISK_SCORE = 'device_risk_score'
    DEVICE_RISK_SCORE_POINTS = 'device_risk_score_points'
    DEVICE_EFFECTIVE_LIKELIHOOD_SUBSCORE = 'device_effective_likelihood_subscore'
    DEVICE_EFFECTIVE_LIKELIHOOD_SUBSCORE_POINTS = 'device_effective_likelihood_subscore_points'
    DEVICE_LIKELIHOOD_SUBSCORE = 'device_likelihood_subscore'
    DEVICE_LIKELIHOOD_SUBSCORE_POINTS = 'device_likelihood_subscore_points'
    DEVICE_IMPACT_SUBSCORE = 'device_impact_subscore'
    DEVICE_IMPACT_SUBSCORE_POINTS = 'device_impact_subscore_points'
    DEVICE_KNOWN_VULNERABILITIES = 'device_known_vulnerabilities'
    DEVICE_KNOWN_VULNERABILITIES_POINTS = 'device_known_vulnerabilities_points'
    DEVICE_INSECURE_PROTOCOLS = 'device_insecure_protocols'
    DEVICE_INSECURE_PROTOCOLS_POINTS = 'device_insecure_protocols_points'
    DEVICE_INTERNET_COMMUNICATION = 'device_internet_communication'
    ALERT_ID = 'alert_id'
    ALERT_TYPE_NAME = 'alert_type_name'
    ALERT_CLASS = 'alert_class'
    ALERT_CATEGORY = 'alert_category'
    ALERT_LABELS = 'alert_labels'
    ALERT_ASSIGNEES = 'alert_assignees'
    DEVICE_ALERT_DETECTED_TIME = 'device_alert_detected_time'
    DEVICE_ALERT_UPDATED_TIME = 'device_alert_updated_time'

    @classmethod
    def from_json(cls, json_str: str) -> DeviceAlertSortableFieldsEnum:
        """Create an instance of DeviceAlertSortableFieldsEnum from a JSON string"""
        return DeviceAlertSortableFieldsEnum(json.loads(json_str))

