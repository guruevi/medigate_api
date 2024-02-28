# GetServersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | **List[object]** |  | 
**count** | **int** |  | [optional] 

## Example

```python
from medigate_api.models.get_servers_response import GetServersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetServersResponse from a JSON string
get_servers_response_instance = GetServersResponse.from_json(json)
# print the JSON string representation of the object
print GetServersResponse.to_json()

# convert the object into a dict
get_servers_response_dict = get_servers_response_instance.to_dict()
# create an instance of GetServersResponse from a dict
get_servers_response_form_dict = get_servers_response.from_dict(get_servers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


