# PublicSetAlertResolutionParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**TargetAlertIds**](TargetAlertIds.md) |  | 
**devices** | [**DeviceFilterBy**](DeviceFilterBy.md) |  | [optional] 
**status** | [**PublicAlertStatus**](PublicAlertStatus.md) | Set the device-alert status to resolve or unresolved. | 

## Example

```python
from medigate_api.models.public_set_alert_resolution_params import PublicSetAlertResolutionParams

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSetAlertResolutionParams from a JSON string
public_set_alert_resolution_params_instance = PublicSetAlertResolutionParams.from_json(json)
# print the JSON string representation of the object
print PublicSetAlertResolutionParams.to_json()

# convert the object into a dict
public_set_alert_resolution_params_dict = public_set_alert_resolution_params_instance.to_dict()
# create an instance of PublicSetAlertResolutionParams from a dict
public_set_alert_resolution_params_form_dict = public_set_alert_resolution_params.from_dict(public_set_alert_resolution_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


