# ValidatingSimpleQueryFilterVulnerabilities

A filter on a single column

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Name of field to filter | 
**operation** | **str** | Type of filter on the field | 
**value** | **object** |  | [optional] 

## Example

```python
from medigate_api.models.validating_simple_query_filter_vulnerabilities import ValidatingSimpleQueryFilterVulnerabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingSimpleQueryFilterVulnerabilities from a JSON string
validating_simple_query_filter_vulnerabilities_instance = ValidatingSimpleQueryFilterVulnerabilities.from_json(json)
# print the JSON string representation of the object
print ValidatingSimpleQueryFilterVulnerabilities.to_json()

# convert the object into a dict
validating_simple_query_filter_vulnerabilities_dict = validating_simple_query_filter_vulnerabilities_instance.to_dict()
# create an instance of ValidatingSimpleQueryFilterVulnerabilities from a dict
validating_simple_query_filter_vulnerabilities_form_dict = validating_simple_query_filter_vulnerabilities.from_dict(validating_simple_query_filter_vulnerabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


