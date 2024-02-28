# DeviceFilterBy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_by** | [**FilterBy**](FilterBy.md) |  | [optional] 

## Example

```python
from medigate_api.models.device_filter_by import DeviceFilterBy

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceFilterBy from a JSON string
device_filter_by_instance = DeviceFilterBy.from_json(json)
# print the JSON string representation of the object
print DeviceFilterBy.to_json()

# convert the object into a dict
device_filter_by_dict = device_filter_by_instance.to_dict()
# create an instance of DeviceFilterBy from a dict
device_filter_by_form_dict = device_filter_by.from_dict(device_filter_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


