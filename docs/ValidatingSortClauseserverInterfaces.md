# ValidatingSortClauseserverInterfaces


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | [**ServerInterfacesSortableFieldsEnum**](ServerInterfacesSortableFieldsEnum.md) | Name of field to sort by | 
**order** | [**SortOrder**](SortOrder.md) | Direction of sort | 

## Example

```python
from medigate_api.models.validating_sort_clauseserver_interfaces import ValidatingSortClauseserverInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingSortClauseserverInterfaces from a JSON string
validating_sort_clauseserver_interfaces_instance = ValidatingSortClauseserverInterfaces.from_json(json)
# print the JSON string representation of the object
print ValidatingSortClauseserverInterfaces.to_json()

# convert the object into a dict
validating_sort_clauseserver_interfaces_dict = validating_sort_clauseserver_interfaces_instance.to_dict()
# create an instance of ValidatingSortClauseserverInterfaces from a dict
validating_sort_clauseserver_interfaces_form_dict = validating_sort_clauseserver_interfaces.from_dict(validating_sort_clauseserver_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


