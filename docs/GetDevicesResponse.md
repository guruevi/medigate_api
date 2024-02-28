# GetDevicesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | **List[object]** |  | 
**count** | **int** |  | [optional] 

## Example

```python
from medigate_api.models.get_devices_response import GetDevicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDevicesResponse from a JSON string
get_devices_response_instance = GetDevicesResponse.from_json(json)
# print the JSON string representation of the object
print GetDevicesResponse.to_json()

# convert the object into a dict
get_devices_response_dict = get_devices_response_instance.to_dict()
# create an instance of GetDevicesResponse from a dict
get_devices_response_form_dict = get_devices_response.from_dict(get_devices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


