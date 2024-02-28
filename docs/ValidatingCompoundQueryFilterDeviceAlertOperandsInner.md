# ValidatingCompoundQueryFilterDeviceAlertOperandsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **object** | Name of field to filter | 
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**value** | **object** |  | [optional] 
**operands** | **object** | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.validating_compound_query_filter_device_alert_operands_inner import ValidatingCompoundQueryFilterDeviceAlertOperandsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingCompoundQueryFilterDeviceAlertOperandsInner from a JSON string
validating_compound_query_filter_device_alert_operands_inner_instance = ValidatingCompoundQueryFilterDeviceAlertOperandsInner.from_json(json)
# print the JSON string representation of the object
print ValidatingCompoundQueryFilterDeviceAlertOperandsInner.to_json()

# convert the object into a dict
validating_compound_query_filter_device_alert_operands_inner_dict = validating_compound_query_filter_device_alert_operands_inner_instance.to_dict()
# create an instance of ValidatingCompoundQueryFilterDeviceAlertOperandsInner from a dict
validating_compound_query_filter_device_alert_operands_inner_form_dict = validating_compound_query_filter_device_alert_operands_inner.from_dict(validating_compound_query_filter_device_alert_operands_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


