# FilterBy4

Filters which devices are returned. Can be a simple filter on a single field, or a combination of several filters for more complex logic.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **object** | Name of field to filter | 
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**value** | **object** |  | [optional] 
**operands** | **object** | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.filter_by4 import FilterBy4

# TODO update the JSON string below
json = "{}"
# create an instance of FilterBy4 from a JSON string
filter_by4_instance = FilterBy4.from_json(json)
# print the JSON string representation of the object
print FilterBy4.to_json()

# convert the object into a dict
filter_by4_dict = filter_by4_instance.to_dict()
# create an instance of FilterBy4 from a dict
filter_by4_form_dict = filter_by4.from_dict(filter_by4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


