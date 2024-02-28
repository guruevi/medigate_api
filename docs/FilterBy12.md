# FilterBy12

Filters which vulnerabilities are matched. Only supports filtering by `id` / `name` fields.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **object** | Name of field to filter | 
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**value** | **object** |  | [optional] 
**operands** | **object** | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.filter_by12 import FilterBy12

# TODO update the JSON string below
json = "{}"
# create an instance of FilterBy12 from a JSON string
filter_by12_instance = FilterBy12.from_json(json)
# print the JSON string representation of the object
print FilterBy12.to_json()

# convert the object into a dict
filter_by12_dict = filter_by12_instance.to_dict()
# create an instance of FilterBy12 from a dict
filter_by12_form_dict = filter_by12.from_dict(filter_by12_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


