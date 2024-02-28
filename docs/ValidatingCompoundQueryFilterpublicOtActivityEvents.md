# ValidatingCompoundQueryFilterpublicOtActivityEvents

A compound filter made up of other filters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**operands** | [**List[ValidatingCompoundQueryFilterpublicOtActivityEventsOperandsInner]**](ValidatingCompoundQueryFilterpublicOtActivityEventsOperandsInner.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.validating_compound_query_filterpublic_ot_activity_events import ValidatingCompoundQueryFilterpublicOtActivityEvents

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingCompoundQueryFilterpublicOtActivityEvents from a JSON string
validating_compound_query_filterpublic_ot_activity_events_instance = ValidatingCompoundQueryFilterpublicOtActivityEvents.from_json(json)
# print the JSON string representation of the object
print ValidatingCompoundQueryFilterpublicOtActivityEvents.to_json()

# convert the object into a dict
validating_compound_query_filterpublic_ot_activity_events_dict = validating_compound_query_filterpublic_ot_activity_events_instance.to_dict()
# create an instance of ValidatingCompoundQueryFilterpublicOtActivityEvents from a dict
validating_compound_query_filterpublic_ot_activity_events_form_dict = validating_compound_query_filterpublic_ot_activity_events.from_dict(validating_compound_query_filterpublic_ot_activity_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


