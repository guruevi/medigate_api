# FilterBy10

Filters which vulnerabilities are matched. Can be a simple filter on a single field, or a combination of several filters for more complex logic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of field to filter | 
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**value** | **object** |  | [optional] 
**operands** | [**List[OperandsInner]**](OperandsInner.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.filter_by10 import FilterBy10

# TODO update the JSON string below
json = "{}"
# create an instance of FilterBy10 from a JSON string
filter_by10_instance = FilterBy10.from_json(json)
# print the JSON string representation of the object
print(FilterBy10.to_json())

# convert the object into a dict
filter_by10_dict = filter_by10_instance.to_dict()
# create an instance of FilterBy10 from a dict
filter_by10_from_dict = FilterBy10.from_dict(filter_by10_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


