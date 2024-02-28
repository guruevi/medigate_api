# SimpleQueryFilter

A filter on a single column

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Name of field to filter | 
**operation** | **str** | Type of filter on the field | 
**value** | **object** |  | [optional] 

## Example

```python
from medigate_api.models.simple_query_filter import SimpleQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleQueryFilter from a JSON string
simple_query_filter_instance = SimpleQueryFilter.from_json(json)
# print the JSON string representation of the object
print SimpleQueryFilter.to_json()

# convert the object into a dict
simple_query_filter_dict = simple_query_filter_instance.to_dict()
# create an instance of SimpleQueryFilter from a dict
simple_query_filter_form_dict = simple_query_filter.from_dict(simple_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


