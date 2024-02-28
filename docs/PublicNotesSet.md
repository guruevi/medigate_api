# PublicNotesSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_specification** | [**TargetSpecification**](TargetSpecification.md) |  | 
**note** | **str** |  | 
**action** | [**NoteAction**](NoteAction.md) |  | [optional] 

## Example

```python
from medigate_api.models.public_notes_set import PublicNotesSet

# TODO update the JSON string below
json = "{}"
# create an instance of PublicNotesSet from a JSON string
public_notes_set_instance = PublicNotesSet.from_json(json)
# print the JSON string representation of the object
print PublicNotesSet.to_json()

# convert the object into a dict
public_notes_set_dict = public_notes_set_instance.to_dict()
# create an instance of PublicNotesSet from a dict
public_notes_set_form_dict = public_notes_set.from_dict(public_notes_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


