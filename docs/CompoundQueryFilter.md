# CompoundQueryFilter

A compound filter made up of other filters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**operands** | [**List[CompoundQueryFilterOperandsInner]**](CompoundQueryFilterOperandsInner.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.compound_query_filter import CompoundQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CompoundQueryFilter from a JSON string
compound_query_filter_instance = CompoundQueryFilter.from_json(json)
# print the JSON string representation of the object
print CompoundQueryFilter.to_json()

# convert the object into a dict
compound_query_filter_dict = compound_query_filter_instance.to_dict()
# create an instance of CompoundQueryFilter from a dict
compound_query_filter_form_dict = compound_query_filter.from_dict(compound_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


