# PublicLabelsSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_specification** | [**TargetSpecification**](TargetSpecification.md) |  | 
**labels_to_add** | **List[str]** |  | [optional] [default to []]
**labels_to_remove** | **List[str]** |  | [optional] [default to []]

## Example

```python
from medigate_api.models.public_labels_set import PublicLabelsSet

# TODO update the JSON string below
json = "{}"
# create an instance of PublicLabelsSet from a JSON string
public_labels_set_instance = PublicLabelsSet.from_json(json)
# print the JSON string representation of the object
print PublicLabelsSet.to_json()

# convert the object into a dict
public_labels_set_dict = public_labels_set_instance.to_dict()
# create an instance of PublicLabelsSet from a dict
public_labels_set_form_dict = public_labels_set.from_dict(public_labels_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


