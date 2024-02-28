# ValidatingSortClauseDeviceAlert


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | [**DeviceAlertSortableFieldsEnum**](DeviceAlertSortableFieldsEnum.md) | Name of field to sort by | 
**order** | [**SortOrder**](SortOrder.md) | Direction of sort | 

## Example

```python
from medigate_api.models.validating_sort_clause_device_alert import ValidatingSortClauseDeviceAlert

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingSortClauseDeviceAlert from a JSON string
validating_sort_clause_device_alert_instance = ValidatingSortClauseDeviceAlert.from_json(json)
# print the JSON string representation of the object
print ValidatingSortClauseDeviceAlert.to_json()

# convert the object into a dict
validating_sort_clause_device_alert_dict = validating_sort_clause_device_alert_instance.to_dict()
# create an instance of ValidatingSortClauseDeviceAlert from a dict
validating_sort_clause_device_alert_form_dict = validating_sort_clause_device_alert.from_dict(validating_sort_clause_device_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


