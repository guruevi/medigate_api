# PublicAlertTargetSpec

A specification of the target objects on which to operate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** | **str** | The type of the target object. | 
**alert_ids** | **List[int]** |  | [optional] 

## Example

```python
from medigate_api.models.public_alert_target_spec import PublicAlertTargetSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PublicAlertTargetSpec from a JSON string
public_alert_target_spec_instance = PublicAlertTargetSpec.from_json(json)
# print the JSON string representation of the object
print PublicAlertTargetSpec.to_json()

# convert the object into a dict
public_alert_target_spec_dict = public_alert_target_spec_instance.to_dict()
# create an instance of PublicAlertTargetSpec from a dict
public_alert_target_spec_form_dict = public_alert_target_spec.from_dict(public_alert_target_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


