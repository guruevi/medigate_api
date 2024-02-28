# GetServerInterfacesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_interfaces** | **List[object]** |  | 
**count** | **int** |  | [optional] 

## Example

```python
from medigate_api.models.get_server_interfaces_response import GetServerInterfacesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetServerInterfacesResponse from a JSON string
get_server_interfaces_response_instance = GetServerInterfacesResponse.from_json(json)
# print the JSON string representation of the object
print GetServerInterfacesResponse.to_json()

# convert the object into a dict
get_server_interfaces_response_dict = get_server_interfaces_response_instance.to_dict()
# create an instance of GetServerInterfacesResponse from a dict
get_server_interfaces_response_form_dict = get_server_interfaces_response.from_dict(get_server_interfaces_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


