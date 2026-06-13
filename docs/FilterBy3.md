# FilterBy3

Filters which devices are returned. Can be a simple filter on a single field, or a combination of several filters for more complex logic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of field to filter | 
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**value** | **object** |  | [optional] 
**operands** | [**List[OperandsInner4]**](OperandsInner4.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.filter_by3 import FilterBy3

# TODO update the JSON string below
json = "{}"
# create an instance of FilterBy3 from a JSON string
filter_by3_instance = FilterBy3.from_json(json)
# print the JSON string representation of the object
print(FilterBy3.to_json())

# convert the object into a dict
filter_by3_dict = filter_by3_instance.to_dict()
# create an instance of FilterBy3 from a dict
filter_by3_from_dict = FilterBy3.from_dict(filter_by3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


