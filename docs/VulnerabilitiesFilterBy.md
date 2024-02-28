# VulnerabilitiesFilterBy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_by** | [**FilterBy12**](FilterBy12.md) |  | 

## Example

```python
from medigate_api.models.vulnerabilities_filter_by import VulnerabilitiesFilterBy

# TODO update the JSON string below
json = "{}"
# create an instance of VulnerabilitiesFilterBy from a JSON string
vulnerabilities_filter_by_instance = VulnerabilitiesFilterBy.from_json(json)
# print the JSON string representation of the object
print VulnerabilitiesFilterBy.to_json()

# convert the object into a dict
vulnerabilities_filter_by_dict = vulnerabilities_filter_by_instance.to_dict()
# create an instance of VulnerabilitiesFilterBy from a dict
vulnerabilities_filter_by_form_dict = vulnerabilities_filter_by.from_dict(vulnerabilities_filter_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


