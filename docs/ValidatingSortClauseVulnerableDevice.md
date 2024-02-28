# ValidatingSortClauseVulnerableDevice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | [**VulnerableDeviceSortableFieldsEnum**](VulnerableDeviceSortableFieldsEnum.md) | Name of field to sort by | 
**order** | [**SortOrder**](SortOrder.md) | Direction of sort | 

## Example

```python
from medigate_api.models.validating_sort_clause_vulnerable_device import ValidatingSortClauseVulnerableDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingSortClauseVulnerableDevice from a JSON string
validating_sort_clause_vulnerable_device_instance = ValidatingSortClauseVulnerableDevice.from_json(json)
# print the JSON string representation of the object
print ValidatingSortClauseVulnerableDevice.to_json()

# convert the object into a dict
validating_sort_clause_vulnerable_device_dict = validating_sort_clause_vulnerable_device_instance.to_dict()
# create an instance of ValidatingSortClauseVulnerableDevice from a dict
validating_sort_clause_vulnerable_device_form_dict = validating_sort_clause_vulnerable_device.from_dict(validating_sort_clause_vulnerable_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


