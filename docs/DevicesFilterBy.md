# DevicesFilterBy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_by** | [**FilterBy**](FilterBy.md) |  | [optional] 

## Example

```python
from medigate_api.models.devices_filter_by import DevicesFilterBy

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesFilterBy from a JSON string
devices_filter_by_instance = DevicesFilterBy.from_json(json)
# print the JSON string representation of the object
print DevicesFilterBy.to_json()

# convert the object into a dict
devices_filter_by_dict = devices_filter_by_instance.to_dict()
# create an instance of DevicesFilterBy from a dict
devices_filter_by_form_dict = devices_filter_by.from_dict(devices_filter_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


