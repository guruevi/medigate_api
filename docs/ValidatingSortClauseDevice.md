# ValidatingSortClauseDevice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | [**DeviceSortableFieldsEnum**](DeviceSortableFieldsEnum.md) | Name of field to sort by | 
**order** | [**SortOrder**](SortOrder.md) | Direction of sort | 

## Example

```python
from medigate_api.models.validating_sort_clause_device import ValidatingSortClauseDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingSortClauseDevice from a JSON string
validating_sort_clause_device_instance = ValidatingSortClauseDevice.from_json(json)
# print the JSON string representation of the object
print ValidatingSortClauseDevice.to_json()

# convert the object into a dict
validating_sort_clause_device_dict = validating_sort_clause_device_instance.to_dict()
# create an instance of ValidatingSortClauseDevice from a dict
validating_sort_clause_device_form_dict = validating_sort_clause_device.from_dict(validating_sort_clause_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


