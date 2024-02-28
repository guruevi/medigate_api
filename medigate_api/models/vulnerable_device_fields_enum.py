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





class VulnerableDeviceFieldsEnum(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    NETWORK_LIST = 'network_list'
    DEVICE_CATEGORY = 'device_category'
    DEVICE_SUBCATEGORY = 'device_subcategory'
    DEVICE_TYPE = 'device_type'
    UID = 'uid'
    ASSET_ID = 'asset_id'
    MAC_LIST = 'mac_list'
    IP_LIST = 'ip_list'
    RISK_SCORE_POINTS = 'risk_score_points'
    RISK_SCORE = 'risk_score'
    DEVICE_TYPE_FAMILY = 'device_type_family'
    MODEL = 'model'
    OS_CATEGORY = 'os_category'
    SERIAL_NUMBER = 'serial_number'
    VLAN_LIST = 'vlan_list'
    RETIRED = 'retired'
    LABELS = 'labels'
    ASSIGNEES = 'assignees'
    SITE_NAME = 'site_name'
    HW_VERSION = 'hw_version'
    LOCAL_NAME = 'local_name'
    OS_NAME = 'os_name'
    OS_VERSION = 'os_version'
    OS_REVISION = 'os_revision'
    OS_SUBCATEGORY = 'os_subcategory'
    COMBINED_OS = 'combined_os'
    ENDPOINT_SECURITY_NAMES = 'endpoint_security_names'
    EQUIPMENT_CLASS = 'equipment_class'
    CONSEQUENCE_OF_FAILURE = 'consequence_of_failure'
    MANAGEMENT_SERVICES = 'management_services'
    AD_DISTINGUISHED_NAME = 'ad_distinguished_name'
    AD_DESCRIPTION = 'ad_description'
    MDM_OWNERSHIP = 'mdm_ownership'
    MDM_ENROLLMENT_STATUS = 'mdm_enrollment_status'
    MDM_COMPLIANCE_STATUS = 'mdm_compliance_status'
    LAST_DOMAIN_USER = 'last_domain_user'
    FDA_CLASS = 'fda_class'
    MOBILITY = 'mobility'
    PURDUE_LEVEL = 'purdue_level'
    DHCP_HOSTNAMES = 'dhcp_hostnames'
    HTTP_HOSTNAMES = 'http_hostnames'
    SNMP_HOSTNAMES = 'snmp_hostnames'
    WINDOWS_HOSTNAMES = 'windows_hostnames'
    OTHER_HOSTNAMES = 'other_hostnames'
    WINDOWS_LAST_SEEN_HOSTNAME = 'windows_last_seen_hostname'
    DHCP_LAST_SEEN_HOSTNAME = 'dhcp_last_seen_hostname'
    HTTP_LAST_SEEN_HOSTNAME = 'http_last_seen_hostname'
    SNMP_LAST_SEEN_HOSTNAME = 'snmp_last_seen_hostname'
    AE_TITLES = 'ae_titles'
    DHCP_FINGERPRINT = 'dhcp_fingerprint'
    NOTE = 'note'
    DOMAINS = 'domains'
    BATTERY_LEVEL = 'battery_level'
    INTERNET_COMMUNICATION = 'internet_communication'
    FINANCIAL_COST = 'financial_cost'
    HANDLES_PII = 'handles_pii'
    MACHINE_TYPE = 'machine_type'
    PHI = 'phi'
    CMMS_STATE = 'cmms_state'
    CMMS_OWNERSHIP = 'cmms_ownership'
    CMMS_ASSET_TAG = 'cmms_asset_tag'
    CMMS_CAMPUS = 'cmms_campus'
    CMMS_BUILDING = 'cmms_building'
    CMMS_LOCATION = 'cmms_location'
    CMMS_FLOOR = 'cmms_floor'
    CMMS_DEPARTMENT = 'cmms_department'
    CMMS_OWNING_COST_CENTER = 'cmms_owning_cost_center'
    CMMS_FINANCIAL_COST = 'cmms_financial_cost'
    CMMS_ROOM = 'cmms_room'
    CMMS_MANUFACTURER = 'cmms_manufacturer'
    CMMS_MODEL = 'cmms_model'
    CMMS_SERIAL_NUMBER = 'cmms_serial_number'
    CMMS_LAST_PM = 'cmms_last_pm'
    CMMS_TECHNICIAN = 'cmms_technician'
    EDR_IS_UP_TO_DATE_TEXT = 'edr_is_up_to_date_text'
    AVG_IN_USE_PER_DAY = 'avg_in_use_per_day'
    AVG_ONLINE_PER_DAY = 'avg_online_per_day'
    AVG_EXAMINATIONS_PER_DAY = 'avg_examinations_per_day'
    MAC_OUI_LIST = 'mac_oui_list'
    IP_ASSIGNMENT_LIST = 'ip_assignment_list'
    PROTOCOL_LOCATION_LIST = 'protocol_location_list'
    VLAN_NAME_LIST = 'vlan_name_list'
    VLAN_DESCRIPTION_LIST = 'vlan_description_list'
    CONNECTION_TYPE_LIST = 'connection_type_list'
    SSID_LIST = 'ssid_list'
    BSSID_LIST = 'bssid_list'
    WIRELESS_ENCRYPTION_TYPE_LIST = 'wireless_encryption_type_list'
    AP_NAME_LIST = 'ap_name_list'
    AP_LOCATION_LIST = 'ap_location_list'
    SWITCH_MAC_LIST = 'switch_mac_list'
    SWITCH_IP_LIST = 'switch_ip_list'
    SWITCH_NAME_LIST = 'switch_name_list'
    SWITCH_PORT_LIST = 'switch_port_list'
    SWITCH_LOCATION_LIST = 'switch_location_list'
    SWITCH_PORT_DESCRIPTION_LIST = 'switch_port_description_list'
    WLC_NAME_LIST = 'wlc_name_list'
    WLC_LOCATION_LIST = 'wlc_location_list'
    APPLIED_ACL_LIST = 'applied_acl_list'
    APPLIED_ACL_TYPE_LIST = 'applied_acl_type_list'
    OPERATING_HOURS_PATTERN_NAME = 'operating_hours_pattern_name'
    COLLECTION_SERVERS = 'collection_servers'
    EDGE_LOCATIONS = 'edge_locations'
    NUMBER_OF_NICS = 'number_of_nics'
    LAST_DOMAIN_USER_ACTIVITY = 'last_domain_user_activity'
    LAST_SCAN_TIME = 'last_scan_time'
    EDR_LAST_SCAN_TIME = 'edr_last_scan_time'
    RETIRED_SINCE = 'retired_since'
    UTILIZATION_RATE = 'utilization_rate'
    ACTIVITY_RATE = 'activity_rate'
    OS_EOL_DATE = 'os_eol_date'
    LAST_SEEN_LIST = 'last_seen_list'
    FIRST_SEEN_LIST = 'first_seen_list'
    WIFI_LAST_SEEN_LIST = 'wifi_last_seen_list'
    LAST_SEEN_ON_SWITCH_LIST = 'last_seen_on_switch_list'
    IS_ONLINE = 'is_online'
    NETWORK_SCOPE_LIST = 'network_scope_list'
    ISE_AUTHENTICATION_METHOD_LIST = 'ise_authentication_method_list'
    ISE_ENDPOINT_PROFILE_LIST = 'ise_endpoint_profile_list'
    ISE_IDENTITY_GROUP_LIST = 'ise_identity_group_list'
    ISE_SECURITY_GROUP_NAME_LIST = 'ise_security_group_name_list'
    ISE_SECURITY_GROUP_TAG_LIST = 'ise_security_group_tag_list'
    ISE_LOGICAL_PROFILE_LIST = 'ise_logical_profile_list'
    CPPM_AUTHENTICATION_STATUS_LIST = 'cppm_authentication_status_list'
    CPPM_ROLES_LIST = 'cppm_roles_list'
    CPPM_SERVICE_LIST = 'cppm_service_list'
    DEVICE_NAME = 'device_name'
    VULNERABILITY_RELEVANCE = 'vulnerability_relevance'
    VULNERABILITY_SOURCE = 'vulnerability_source'
    VULNERABILITY_LAST_UPDATED = 'vulnerability_last_updated'
    MANUFACTURER = 'manufacturer'
    EFFECTIVE_LIKELIHOOD_SUBSCORE = 'effective_likelihood_subscore'
    EFFECTIVE_LIKELIHOOD_SUBSCORE_POINTS = 'effective_likelihood_subscore_points'
    LIKELIHOOD_SUBSCORE = 'likelihood_subscore'
    LIKELIHOOD_SUBSCORE_POINTS = 'likelihood_subscore_points'
    IMPACT_SUBSCORE = 'impact_subscore'
    IMPACT_SUBSCORE_POINTS = 'impact_subscore_points'
    KNOWN_VULNERABILITIES = 'known_vulnerabilities'
    KNOWN_VULNERABILITIES_POINTS = 'known_vulnerabilities_points'
    INSECURE_PROTOCOLS = 'insecure_protocols'
    INSECURE_PROTOCOLS_POINTS = 'insecure_protocols_points'
    SUSPICIOUS = 'suspicious'
    SWITCH_GROUP_NAME_LIST = 'switch_group_name_list'
    SWITCH_DEVICE_TYPE_LIST = 'switch_device_type_list'
    CMDB_ASSET_TAG = 'cmdb_asset_tag'
    INFECTED = 'infected'
    MANAGED_BY = 'managed_by'
    AUTHENTICATION_USER_LIST = 'authentication_user_list'
    COLLECTION_INTERFACES = 'collection_interfaces'
    SLOT_CARDS = 'slot_cards'
    SOFTWARE_OR_FIRMWARE_VERSION = 'software_or_firmware_version'
    ENFORCEMENT_OR_AUTHORIZATION_PROFILES_LIST = 'enforcement_or_authorization_profiles_list'
    ISE_SECURITY_GROUP_DESCRIPTION_LIST = 'ise_security_group_description_list'
    RECOMMENDED_FIREWALL_GROUP_NAME = 'recommended_firewall_group_name'
    ORGANIZATION_FIREWALL_GROUP_NAME = 'organization_firewall_group_name'
    RECOMMENDED_ZONE_NAME = 'recommended_zone_name'
    ORGANIZATION_ZONE_NAME = 'organization_zone_name'
    VULNERABILITY_LAST_CHANGED = 'vulnerability_last_changed'
    VULNERABILITY_STATUS = 'vulnerability_status'
    LESS_THAN_THE_CUSTOM_ATTRIBUTE_API_NAME_DEFINED_IN_THE_DASHBOARD_COMMA__INCLUDING_THE_PREFIX_BACK_SLASH_DOUBLE_QUOTE_CUSTOM_ATTRIBUTE_BACK_SLASH_DOUBLE_QUOTE_GREATER_THAN = '<the custom attribute api name defined in the dashboard, including the prefix \"custom_attribute_\">'

    @classmethod
    def from_json(cls, json_str: str) -> VulnerableDeviceFieldsEnum:
        """Create an instance of VulnerableDeviceFieldsEnum from a JSON string"""
        return VulnerableDeviceFieldsEnum(json.loads(json_str))


