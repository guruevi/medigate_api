# PublicSetCustomAttributeParams

The base class for parameters to a user annotations endpoint, specifying the target of the operation.  The target_specification is often a subclass of TargetSpec which includes a specification of exactly which targets should be operated on, such as a group of pagination parameters or a set of ids, but at the very minimum it must include the target type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_specification** | [**PublicDeviceTargetSpec**](PublicDeviceTargetSpec.md) |  | 
**custom_attribute_api_name** | **str** | The API name of the custom attribute whose value should be set. | 
**value** | **str** | The value to store to the custom attribute. Can be &#x60;null&#x60; to clear the existing value. | 

## Example

```python
from medigate_api.models.public_set_custom_attribute_params import PublicSetCustomAttributeParams

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSetCustomAttributeParams from a JSON string
public_set_custom_attribute_params_instance = PublicSetCustomAttributeParams.from_json(json)
# print the JSON string representation of the object
print PublicSetCustomAttributeParams.to_json()

# convert the object into a dict
public_set_custom_attribute_params_dict = public_set_custom_attribute_params_instance.to_dict()
# create an instance of PublicSetCustomAttributeParams from a dict
public_set_custom_attribute_params_form_dict = public_set_custom_attribute_params.from_dict(public_set_custom_attribute_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


