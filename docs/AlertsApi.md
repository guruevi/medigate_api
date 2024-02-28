# medigate_api.AlertsApi

All URIs are relative to *https://api.medigate.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_devices_api_v1_alerts_alert_id_devices_post**](AlertsApi.md#get_alert_devices_api_v1_alerts_alert_id_devices_post) | **POST** /api/v1/alerts/{alert_id}/devices | Get devices affected by an alert
[**get_alerts_api_v1_alerts_post**](AlertsApi.md#get_alerts_api_v1_alerts_post) | **POST** /api/v1/alerts/ | Get details of alerts
[**set_alert_resolution_api_v1_device_alert_status_set_post**](AlertsApi.md#set_alert_resolution_api_v1_device_alert_status_set_post) | **POST** /api/v1/device-alert-status/set | Set status for device alert relations


# **get_alert_devices_api_v1_alerts_alert_id_devices_post**
> GetAlertedDevicesResponse get_alert_devices_api_v1_alerts_alert_id_devices_post(alert_id, get_alerted_devices_parameters)

Get devices affected by an alert

Get devices affected by an alert. This endpoint returns similar data to the [Get details of devices][1] endpoint, except that only affected devices are returned. There is also an additional device field indicating if the alert is resolved for the device.  ### Fields supported by this endpoint All fields supported by [Get details of devices][1] endpoint, and additionally:  | Field         | Description                                                                              | Supported Operations                                        | |---------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------| | `is_resolved` | A boolean field indicating if the alert triggered for a device is resolved or unresolved | `is_null`,`not_equals`,`is_not_null`,`not_in`,`equals`,`in` |   [1]: #operation/get_devices

### Example

* Bearer Authentication (CustomHTTPBearer):
```python
import time
import os
import medigate_api
from medigate_api.models.get_alerted_devices_parameters import GetAlertedDevicesParameters
from medigate_api.models.get_alerted_devices_response import GetAlertedDevicesResponse
from medigate_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.medigate.io
# See configuration.py for a list of all supported configuration parameters.
configuration = medigate_api.Configuration(
    host = "https://api.medigate.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: CustomHTTPBearer
configuration = medigate_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with medigate_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = medigate_api.AlertsApi(api_client)
    alert_id = 56 # int | Alert ID, as indicated in the `id` field of an alert
    get_alerted_devices_parameters = {offset=0, limit=100, fields=[id, alert_name, alert_type_name, alert_class, category, detected_time, updated_time, devices_count, unresolved_devices_count, medical_devices_count, iot_devices_count, it_devices_count, ot_devices_count, status, malicious_ip_tags_list]} # GetAlertedDevicesParameters | 

    try:
        # Get devices affected by an alert
        api_response = api_instance.get_alert_devices_api_v1_alerts_alert_id_devices_post(alert_id, get_alerted_devices_parameters)
        print("The response of AlertsApi->get_alert_devices_api_v1_alerts_alert_id_devices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert_devices_api_v1_alerts_alert_id_devices_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| Alert ID, as indicated in the &#x60;id&#x60; field of an alert | 
 **get_alerted_devices_parameters** | [**GetAlertedDevicesParameters**](GetAlertedDevicesParameters.md)|  | 

### Return type

[**GetAlertedDevicesResponse**](GetAlertedDevicesResponse.md)

### Authorization

[CustomHTTPBearer](../README.md#CustomHTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_api_v1_alerts_post**
> GetAlertsResponse get_alerts_api_v1_alerts_post(get_alerts_parameters)

Get details of alerts

The data returned by this endpoint corresponds to the Alerts table in the dashboard.  Alerts are returned in ascending Alert ID order.  ### Fields supported by this endpoint  <details><summary>Click to expand</summary>  | Field                      | Description                                                                                                                                           | Supported Operations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | |----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `id`                       | Platform unique Alert ID                                                                                                                              | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                                                                                                                                                                                                                                                                                                                             | | `alert_name`               | The alert name, such as “Malicious Internet Communication: 62.172.138.35”                                                                             | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                                                                                                                                                                                                                                                                                                                                                         | | `alert_type_name`          | An alert type such as \"Outdated Firmware\"                                                                                                             | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                                                                                                                                                                                                                                                                                                                                                         | | `alert_class`              | The alert class, such as “Pre-Defined Alerts” and “Custom Alerts”                                                                                     | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                                                                                                                                                                                                                                                                                                                                                         | | `category`                 | Alert category such as \"Risk\" or \"Segmentation\"                                                                                                       | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                                                                                                                                                                                                                                                                                                                                                         | | `detected_time`            | Date and time when the Alert was first detected                                                                                                       | `not_equals`,`after_seconds_from_now`,`less_or_equal`,`after_seconds_ago`,`greater_or_equal`,`not_between`,`is_null`,`before`,`after`,`is_not_null`,`equals`,`before_seconds_ago`,`not_in`,`between`,`less`,`greater`,`before_seconds_from_now`,`in`                                                                                                                                                                                                                                                                                                      | | `updated_time`             | Date and time of last Alert update                                                                                                                    | `not_equals`,`after_seconds_from_now`,`less_or_equal`,`after_seconds_ago`,`greater_or_equal`,`not_between`,`is_null`,`before`,`after`,`is_not_null`,`equals`,`before_seconds_ago`,`not_in`,`between`,`less`,`greater`,`before_seconds_from_now`,`in`                                                                                                                                                                                                                                                                                                      | | `devices_count`            | Number of total affected devices                                                                                                                      | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                                                                                                                                                                                                                                                                                                                             | | `unresolved_devices_count` | Number of unresolved devices                                                                                                                          | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                                                                                                                                                                                                                                                                                                                             | | `medical_devices_count`    | Number of affected Medical devices                                                                                                                    | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                                                                                                                                                                                                                                                                                                                             | | `iot_devices_count`        | Number of affected IoT devices                                                                                                                        | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                                                                                                                                                                                                                                                                                                                             | | `it_devices_count`         | Number of affected IT devices                                                                                                                         | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                                                                                                                                                                                                                                                                                                                             | | `ot_devices_count`         | Number of affected OT devices                                                                                                                         | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                                                                                                                                                                                                                                                                                                                             | | `status`                   | Alert status such as \"Resolved\" or \"Acknowledged\"                                                                                                     | _Not filterable_                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | | `malicious_ip_tags_list`   | The Malicious IP Tags, powered by Anomali, associated with the Attempted Malicious Internet Communication and Malicious Internet Communication alerts | `has_any_not_ends_with`,`has_only_ends_with`,`has_only_equals`,`has_none_contains`,`equals`,`has_only_starts_with`,`contains`,`has_only_contains`,`has_none_ends_with`,`has_all_equals`,`not_contains`,`superset_of`,`none_equal`,`in`,`has_none_equals`,`starts_with`,`not_equals`,`has_none_starts_with`,`has_any_not_contains`,`is_null`,`has_any_contains`,`has_any_ends_with`,`is_not_null`,`all_equal`,`has_any_equals`,`ends_with`,`not_in`,`has_any_not_equals`,`not_ends_with`,`has_any_starts_with`,`has_any_not_starts_with`,`not_starts_with` |  </details>

### Example

* Bearer Authentication (CustomHTTPBearer):
```python
import time
import os
import medigate_api
from medigate_api.models.get_alerts_parameters import GetAlertsParameters
from medigate_api.models.get_alerts_response import GetAlertsResponse
from medigate_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.medigate.io
# See configuration.py for a list of all supported configuration parameters.
configuration = medigate_api.Configuration(
    host = "https://api.medigate.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: CustomHTTPBearer
configuration = medigate_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with medigate_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = medigate_api.AlertsApi(api_client)
    get_alerts_parameters = {"offset":0,"limit":100,"fields":["id","alert_name","alert_type_name","alert_class","category","detected_time","updated_time","devices_count","unresolved_devices_count","medical_devices_count","iot_devices_count","it_devices_count","ot_devices_count","status","malicious_ip_tags_list"]} # GetAlertsParameters | 

    try:
        # Get details of alerts
        api_response = api_instance.get_alerts_api_v1_alerts_post(get_alerts_parameters)
        print("The response of AlertsApi->get_alerts_api_v1_alerts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alerts_api_v1_alerts_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_alerts_parameters** | [**GetAlertsParameters**](GetAlertsParameters.md)|  | 

### Return type

[**GetAlertsResponse**](GetAlertsResponse.md)

### Authorization

[CustomHTTPBearer](../README.md#CustomHTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_alert_resolution_api_v1_device_alert_status_set_post**
> object set_alert_resolution_api_v1_device_alert_status_set_post(public_set_alert_resolution_params)

Set status for device alert relations

Set device-alert status to resolved or unresolved. If no filter_by parameter is provided, this API call will resolve or unresolve all device-alert relations for the specified alert IDs. if a filter_by parameter is provided, the API call will exclusively resolve or unresolve device-alert relations that meet the specified filter criteria   ### Fields supported by this endpoint All fields supported by [Get details of devices][1].  [1]: #operation/get_devices

### Example

* Bearer Authentication (CustomHTTPBearer):
```python
import time
import os
import medigate_api
from medigate_api.models.public_set_alert_resolution_params import PublicSetAlertResolutionParams
from medigate_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.medigate.io
# See configuration.py for a list of all supported configuration parameters.
configuration = medigate_api.Configuration(
    host = "https://api.medigate.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: CustomHTTPBearer
configuration = medigate_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with medigate_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = medigate_api.AlertsApi(api_client)
    public_set_alert_resolution_params = medigate_api.PublicSetAlertResolutionParams() # PublicSetAlertResolutionParams | 

    try:
        # Set status for device alert relations
        api_response = api_instance.set_alert_resolution_api_v1_device_alert_status_set_post(public_set_alert_resolution_params)
        print("The response of AlertsApi->set_alert_resolution_api_v1_device_alert_status_set_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->set_alert_resolution_api_v1_device_alert_status_set_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_set_alert_resolution_params** | [**PublicSetAlertResolutionParams**](PublicSetAlertResolutionParams.md)|  | 

### Return type

**object**

### Authorization

[CustomHTTPBearer](../README.md#CustomHTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

