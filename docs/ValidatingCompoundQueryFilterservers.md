# ValidatingCompoundQueryFilterservers

A compound filter made up of other filters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**operands** | [**List[ValidatingCompoundQueryFilterserversOperandsInner]**](ValidatingCompoundQueryFilterserversOperandsInner.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.validating_compound_query_filterservers import ValidatingCompoundQueryFilterservers

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingCompoundQueryFilterservers from a JSON string
validating_compound_query_filterservers_instance = ValidatingCompoundQueryFilterservers.from_json(json)
# print the JSON string representation of the object
print ValidatingCompoundQueryFilterservers.to_json()

# convert the object into a dict
validating_compound_query_filterservers_dict = validating_compound_query_filterservers_instance.to_dict()
# create an instance of ValidatingCompoundQueryFilterservers from a dict
validating_compound_query_filterservers_form_dict = validating_compound_query_filterservers.from_dict(validating_compound_query_filterservers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


