# ValidatingSimpleQueryFilterserverInterfaces

A filter on a single column

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Name of field to filter | 
**operation** | **str** | Type of filter on the field | 
**value** | **object** |  | [optional] 

## Example

```python
from medigate_api.models.validating_simple_query_filterserver_interfaces import ValidatingSimpleQueryFilterserverInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingSimpleQueryFilterserverInterfaces from a JSON string
validating_simple_query_filterserver_interfaces_instance = ValidatingSimpleQueryFilterserverInterfaces.from_json(json)
# print the JSON string representation of the object
print ValidatingSimpleQueryFilterserverInterfaces.to_json()

# convert the object into a dict
validating_simple_query_filterserver_interfaces_dict = validating_simple_query_filterserver_interfaces_instance.to_dict()
# create an instance of ValidatingSimpleQueryFilterserverInterfaces from a dict
validating_simple_query_filterserver_interfaces_form_dict = validating_simple_query_filterserver_interfaces.from_dict(validating_simple_query_filterserver_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


