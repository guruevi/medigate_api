# PublicAssigneesSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_specification** | [**TargetSpecification**](TargetSpecification.md) |  | 
**usernames_to_add** | **List[str]** |  | [optional] [default to []]
**usernames_to_remove** | **List[str]** |  | [optional] [default to []]
**group_names_to_add** | **List[str]** |  | [optional] [default to []]
**group_names_to_remove** | **List[str]** |  | [optional] [default to []]

## Example

```python
from medigate_api.models.public_assignees_set import PublicAssigneesSet

# TODO update the JSON string below
json = "{}"
# create an instance of PublicAssigneesSet from a JSON string
public_assignees_set_instance = PublicAssigneesSet.from_json(json)
# print the JSON string representation of the object
print PublicAssigneesSet.to_json()

# convert the object into a dict
public_assignees_set_dict = public_assignees_set_instance.to_dict()
# create an instance of PublicAssigneesSet from a dict
public_assignees_set_form_dict = public_assignees_set.from_dict(public_assignees_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


