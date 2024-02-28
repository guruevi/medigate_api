# GetDevicesParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_by** | [**FilterBy5**](FilterBy5.md) |  | [optional] 
**fields** | [**List[DeviceFieldsEnum]**](DeviceFieldsEnum.md) | Specify which fields to return for each item. See the endpoint description for details of supported fields. | 
**sort_by** | [**List[ValidatingSortClauseDevice]**](ValidatingSortClauseDevice.md) | Specifies how the returned data should be sorted. If more than one sort clause is passed, additional clauses will be used to sort data that is equal in all previous clauses. | [optional] [default to [{field=uid, order=asc}]]
**offset** | **int** | An offset in the data. This can be used to fetch all data in a paginated manner, by e.g requesting (offset&#x3D;0, limit&#x3D;100) followed by (offset&#x3D;100, limit&#x3D;100), (offset&#x3D;200, limit&#x3D;100), etc. | [optional] [default to 0]
**limit** | **int** | Maximum amount of items to fetch | [optional] [default to 100]
**include_count** | **bool** |  | [optional] [default to False]

## Example

```python
from medigate_api.models.get_devices_parameters import GetDevicesParameters

# TODO update the JSON string below
json = "{}"
# create an instance of GetDevicesParameters from a JSON string
get_devices_parameters_instance = GetDevicesParameters.from_json(json)
# print the JSON string representation of the object
print GetDevicesParameters.to_json()

# convert the object into a dict
get_devices_parameters_dict = get_devices_parameters_instance.to_dict()
# create an instance of GetDevicesParameters from a dict
get_devices_parameters_form_dict = get_devices_parameters.from_dict(get_devices_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


