# ValidatingCompoundQueryFilterVulnerableDevice

A compound filter made up of other filters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**operands** | [**List[ValidatingCompoundQueryFilterVulnerableDeviceOperandsInner]**](ValidatingCompoundQueryFilterVulnerableDeviceOperandsInner.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.validating_compound_query_filter_vulnerable_device import ValidatingCompoundQueryFilterVulnerableDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingCompoundQueryFilterVulnerableDevice from a JSON string
validating_compound_query_filter_vulnerable_device_instance = ValidatingCompoundQueryFilterVulnerableDevice.from_json(json)
# print the JSON string representation of the object
print ValidatingCompoundQueryFilterVulnerableDevice.to_json()

# convert the object into a dict
validating_compound_query_filter_vulnerable_device_dict = validating_compound_query_filter_vulnerable_device_instance.to_dict()
# create an instance of ValidatingCompoundQueryFilterVulnerableDevice from a dict
validating_compound_query_filter_vulnerable_device_form_dict = validating_compound_query_filter_vulnerable_device.from_dict(validating_compound_query_filter_vulnerable_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


