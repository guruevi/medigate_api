# ValidatingCompoundQueryFilterVulnerabilities

A compound filter made up of other filters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**operands** | [**List[ValidatingCompoundQueryFilterVulnerabilitiesOperandsInner]**](ValidatingCompoundQueryFilterVulnerabilitiesOperandsInner.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.validating_compound_query_filter_vulnerabilities import ValidatingCompoundQueryFilterVulnerabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingCompoundQueryFilterVulnerabilities from a JSON string
validating_compound_query_filter_vulnerabilities_instance = ValidatingCompoundQueryFilterVulnerabilities.from_json(json)
# print the JSON string representation of the object
print ValidatingCompoundQueryFilterVulnerabilities.to_json()

# convert the object into a dict
validating_compound_query_filter_vulnerabilities_dict = validating_compound_query_filter_vulnerabilities_instance.to_dict()
# create an instance of ValidatingCompoundQueryFilterVulnerabilities from a dict
validating_compound_query_filter_vulnerabilities_form_dict = validating_compound_query_filter_vulnerabilities.from_dict(validating_compound_query_filter_vulnerabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


