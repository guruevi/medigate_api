# FilterBy11

Filters which vulnerabilities are matched. Only supports filtering by `id` / `name` fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of field to filter | 
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**value** | **object** |  | [optional] 
**operands** | [**List[OperandsInner6]**](OperandsInner6.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.filter_by11 import FilterBy11

# TODO update the JSON string below
json = "{}"
# create an instance of FilterBy11 from a JSON string
filter_by11_instance = FilterBy11.from_json(json)
# print the JSON string representation of the object
print(FilterBy11.to_json())

# convert the object into a dict
filter_by11_dict = filter_by11_instance.to_dict()
# create an instance of FilterBy11 from a dict
filter_by11_from_dict = FilterBy11.from_dict(filter_by11_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


