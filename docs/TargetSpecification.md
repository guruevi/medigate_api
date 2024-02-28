# TargetSpecification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** | **object** | The type of the target object. | 
**filter_by** | [**FilterBy11**](FilterBy11.md) |  | [optional] 
**alert_ids** | **object** |  | [optional] 

## Example

```python
from medigate_api.models.target_specification import TargetSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of TargetSpecification from a JSON string
target_specification_instance = TargetSpecification.from_json(json)
# print the JSON string representation of the object
print TargetSpecification.to_json()

# convert the object into a dict
target_specification_dict = target_specification_instance.to_dict()
# create an instance of TargetSpecification from a dict
target_specification_form_dict = target_specification.from_dict(target_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


