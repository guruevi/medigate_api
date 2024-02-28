# ValidatingSortClauseAlertedDevice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | [**AlertedDeviceSortableFieldsEnum**](AlertedDeviceSortableFieldsEnum.md) | Name of field to sort by | 
**order** | [**SortOrder**](SortOrder.md) | Direction of sort | 

## Example

```python
from medigate_api.models.validating_sort_clause_alerted_device import ValidatingSortClauseAlertedDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingSortClauseAlertedDevice from a JSON string
validating_sort_clause_alerted_device_instance = ValidatingSortClauseAlertedDevice.from_json(json)
# print the JSON string representation of the object
print ValidatingSortClauseAlertedDevice.to_json()

# convert the object into a dict
validating_sort_clause_alerted_device_dict = validating_sort_clause_alerted_device_instance.to_dict()
# create an instance of ValidatingSortClauseAlertedDevice from a dict
validating_sort_clause_alerted_device_form_dict = validating_sort_clause_alerted_device.from_dict(validating_sort_clause_alerted_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


