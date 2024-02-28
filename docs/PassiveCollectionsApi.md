# medigate_api.PassiveCollectionsApi

All URIs are relative to *https://api.medigate.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_servers_api_v1_server_interfaces_post**](PassiveCollectionsApi.md#get_servers_api_v1_server_interfaces_post) | **POST** /api/v1/server_interfaces/ | Get server interfaces
[**get_servers_api_v1_servers_post**](PassiveCollectionsApi.md#get_servers_api_v1_servers_post) | **POST** /api/v1/servers/ | Get details of servers


# **get_servers_api_v1_server_interfaces_post**
> GetServerInterfacesResponse get_servers_api_v1_server_interfaces_post(get_server_interfaces_parameters)

Get server interfaces

Get details of server interfaces from the database. The data returned by this endpoint corresponds to the Server Interfaces table in the dashboard.  ### Fields supported by this endpoint  <details><summary>Click to expand</summary>  | Field                         | Description                                                                                                | Supported Operations                                                                                                                                                                                                          | |-------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `server_name`                 | Indicates the collection server name that is set during deployment                                         | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                             | | `interface_name`              | Indicates the name of the interface                                                                        | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                             | | `interface_status`            | Indicates the availability status of the interface: Up, No Carrier                                         | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                             | | `interface_type`              | Indicates the types of interface: SPAN, Management                                                         | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                             | | `interface_connection_type`   | Indicates how the interface is connected to the network: SFP+, RJ45 (Copper)                               | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                             | | `avg_traffic_past_month_mbps` | Indicates the average volume in megabits per second (Mbps) of traffic sent to the server in the past month | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in` | | `avg_traffic_past_week_mbps`  | Indicates the average volume in megabits per second (Mbps) of traffic sent to the server in the past week  | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in` | | `avg_traffic_past_hour_mbps`  | Indicates the average volume in megabits per second (Mbps) of traffic sent to the server in the past hour  | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in` | | `notes`                       | Notes about the interface                                                                                  | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                             |  </details>

### Example

* Bearer Authentication (CustomHTTPBearer):
```python
import time
import os
import medigate_api
from medigate_api.models.get_server_interfaces_parameters import GetServerInterfacesParameters
from medigate_api.models.get_server_interfaces_response import GetServerInterfacesResponse
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
    api_instance = medigate_api.PassiveCollectionsApi(api_client)
    get_server_interfaces_parameters = {"offset":0,"limit":100,"fields":["server_name","interface_name","interface_status","interface_type","interface_connection_type","avg_traffic_past_month_mbps","avg_traffic_past_week_mbps","avg_traffic_past_hour_mbps","notes"]} # GetServerInterfacesParameters | 

    try:
        # Get server interfaces
        api_response = api_instance.get_servers_api_v1_server_interfaces_post(get_server_interfaces_parameters)
        print("The response of PassiveCollectionsApi->get_servers_api_v1_server_interfaces_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PassiveCollectionsApi->get_servers_api_v1_server_interfaces_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_server_interfaces_parameters** | [**GetServerInterfacesParameters**](GetServerInterfacesParameters.md)|  | 

### Return type

[**GetServerInterfacesResponse**](GetServerInterfacesResponse.md)

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

# **get_servers_api_v1_servers_post**
> GetServersResponse get_servers_api_v1_servers_post(get_servers_parameters)

Get details of servers

Get details of servers from the database. The data returned by this endpoint corresponds to the Servers table in the dashboard.  ### Fields supported by this endpoint  <details><summary>Click to expand</summary>  | Field                         | Description                                                                                                | Supported Operations                                                                                                                                                                                                                                      | |-------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `server_name`                 | Indicates the collection server name that is set during deployment                                         | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                                                         | | `server_location`             | The physical location of each server                                                                       | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                                                         | | `server_status`               | Indicates the operational status of the server: Up, Down and Pending                                       | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                                                         | | `model`                       | Indicates the server model, such as: MCS R340 or R640                                                      | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                                                         | | `os_version`                  | Ubuntu Operating System version                                                                            | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                                                         | | `serial_number`               | Server serial number                                                                                       | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                                                         | | `num_of_interfaces`           | The number of interfaces of the collection server                                                          | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                             | | `management_ip`               | Indicates the Data/Management port IP address                                                              | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`between`,`less`,`not_ends_with`,`not_contains`,`greater`,`not_in_subnet`,`not_starts_with`,`in_subnet`,`in` | | `idrac_ip`                    | Indicates the IP address of the Integrated Dell Remote Access Controller (IDRAC)                           | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`between`,`less`,`not_ends_with`,`not_contains`,`greater`,`not_in_subnet`,`not_starts_with`,`in_subnet`,`in` | | `management_mac`              | Indicates the Data/Management port MAC address                                                             | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                             | | `uptime_days`                 | Indicates the number of days the server is up                                                              | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                             | | `avg_traffic_past_month_mbps` | Indicates the average volume in megabits per second (Mbps) of traffic sent to the server in the past month | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                             | | `avg_traffic_past_week_mbps`  | Indicates the average volume in megabits per second (Mbps) of traffic sent to the server in the past week  | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                             | | `avg_traffic_past_hour_mbps`  | Indicates the average volume in megabits per second (Mbps) of traffic sent to the server in the past hour  | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                             | | `num_of_open_incidents`       | Indicates the number of open incidents                                                                     | `starts_with`,`not_equals`,`less_or_equal`,`greater_or_equal`,`not_between`,`is_null`,`is_not_null`,`equals`,`contains`,`ends_with`,`not_in`,`less`,`between`,`not_ends_with`,`not_contains`,`greater`,`not_starts_with`,`in`                             | | `notes`                       | Notes about the server                                                                                     | `starts_with`,`not_equals`,`ends_with`,`not_in`,`not_ends_with`,`not_contains`,`is_null`,`not_starts_with`,`is_not_null`,`equals`,`in`,`contains`                                                                                                         |  </details>

### Example

* Bearer Authentication (CustomHTTPBearer):
```python
import time
import os
import medigate_api
from medigate_api.models.get_servers_parameters import GetServersParameters
from medigate_api.models.get_servers_response import GetServersResponse
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
    api_instance = medigate_api.PassiveCollectionsApi(api_client)
    get_servers_parameters = {"offset":0,"limit":100,"fields":["server_name","server_location","server_status","model","os_version","serial_number","num_of_interfaces","management_ip","idrac_ip","management_mac","uptime_days","avg_traffic_past_month_mbps","avg_traffic_past_week_mbps","avg_traffic_past_hour_mbps","num_of_open_incidents","notes"]} # GetServersParameters | 

    try:
        # Get details of servers
        api_response = api_instance.get_servers_api_v1_servers_post(get_servers_parameters)
        print("The response of PassiveCollectionsApi->get_servers_api_v1_servers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PassiveCollectionsApi->get_servers_api_v1_servers_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_servers_parameters** | [**GetServersParameters**](GetServersParameters.md)|  | 

### Return type

[**GetServersResponse**](GetServersResponse.md)

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

