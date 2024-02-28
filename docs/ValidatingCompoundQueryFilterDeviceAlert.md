# ValidatingCompoundQueryFilterDeviceAlert

A compound filter made up of other filters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**operands** | [**List[ValidatingCompoundQueryFilterDeviceAlertOperandsInner]**](ValidatingCompoundQueryFilterDeviceAlertOperandsInner.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.validating_compound_query_filter_device_alert import ValidatingCompoundQueryFilterDeviceAlert

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingCompoundQueryFilterDeviceAlert from a JSON string
validating_compound_query_filter_device_alert_instance = ValidatingCompoundQueryFilterDeviceAlert.from_json(json)
# print the JSON string representation of the object
print ValidatingCompoundQueryFilterDeviceAlert.to_json()

# convert the object into a dict
validating_compound_query_filter_device_alert_dict = validating_compound_query_filter_device_alert_instance.to_dict()
# create an instance of ValidatingCompoundQueryFilterDeviceAlert from a dict
validating_compound_query_filter_device_alert_form_dict = validating_compound_query_filter_device_alert.from_dict(validating_compound_query_filter_device_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


