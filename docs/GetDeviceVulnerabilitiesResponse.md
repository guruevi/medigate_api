# GetDeviceVulnerabilitiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices_vulnerabilities** | **List[object]** |  | 
**count** | **int** |  | [optional] 

## Example

```python
from medigate_api.models.get_device_vulnerabilities_response import GetDeviceVulnerabilitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceVulnerabilitiesResponse from a JSON string
get_device_vulnerabilities_response_instance = GetDeviceVulnerabilitiesResponse.from_json(json)
# print the JSON string representation of the object
print GetDeviceVulnerabilitiesResponse.to_json()

# convert the object into a dict
get_device_vulnerabilities_response_dict = get_device_vulnerabilities_response_instance.to_dict()
# create an instance of GetDeviceVulnerabilitiesResponse from a dict
get_device_vulnerabilities_response_form_dict = get_device_vulnerabilities_response.from_dict(get_device_vulnerabilities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


