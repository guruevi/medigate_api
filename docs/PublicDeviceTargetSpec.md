# PublicDeviceTargetSpec

A specification of the target objects on which to operate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** | **str** | The type of the target object. | 
**filter_by** | [**FilterBy**](FilterBy.md) |  | [optional] 

## Example

```python
from medigate_api.models.public_device_target_spec import PublicDeviceTargetSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PublicDeviceTargetSpec from a JSON string
public_device_target_spec_instance = PublicDeviceTargetSpec.from_json(json)
# print the JSON string representation of the object
print PublicDeviceTargetSpec.to_json()

# convert the object into a dict
public_device_target_spec_dict = public_device_target_spec_instance.to_dict()
# create an instance of PublicDeviceTargetSpec from a dict
public_device_target_spec_form_dict = public_device_target_spec.from_dict(public_device_target_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


