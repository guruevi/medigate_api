# GetVulnerabilitiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vulnerabilities** | **List[object]** |  | 
**count** | **int** |  | [optional] 

## Example

```python
from medigate_api.models.get_vulnerabilities_response import GetVulnerabilitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetVulnerabilitiesResponse from a JSON string
get_vulnerabilities_response_instance = GetVulnerabilitiesResponse.from_json(json)
# print the JSON string representation of the object
print GetVulnerabilitiesResponse.to_json()

# convert the object into a dict
get_vulnerabilities_response_dict = get_vulnerabilities_response_instance.to_dict()
# create an instance of GetVulnerabilitiesResponse from a dict
get_vulnerabilities_response_form_dict = get_vulnerabilities_response.from_dict(get_vulnerabilities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


