# GetDeviceAlertsParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_by** | [**FilterBy3**](FilterBy3.md) |  | [optional] 
**fields** | [**List[DeviceAlertFieldsEnum]**](DeviceAlertFieldsEnum.md) | Specify which fields to return for each item. See the endpoint description for details of supported fields. | 
**sort_by** | [**List[ValidatingSortClauseDeviceAlert]**](ValidatingSortClauseDeviceAlert.md) | Specifies how the returned data should be sorted. If more than one sort clause is passed, additional clauses will be used to sort data that is equal in all previous clauses. | [optional] [default to [{field=device_uid, order=asc}, {field=alert_id, order=asc}]]
**offset** | **int** | An offset in the data. This can be used to fetch all data in a paginated manner, by e.g requesting (offset&#x3D;0, limit&#x3D;100) followed by (offset&#x3D;100, limit&#x3D;100), (offset&#x3D;200, limit&#x3D;100), etc. | [optional] [default to 0]
**limit** | **int** | Maximum amount of items to fetch | [optional] [default to 100]
**include_count** | **bool** |  | [optional] [default to False]

## Example

```python
from medigate_api.models.get_device_alerts_parameters import GetDeviceAlertsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceAlertsParameters from a JSON string
get_device_alerts_parameters_instance = GetDeviceAlertsParameters.from_json(json)
# print the JSON string representation of the object
print GetDeviceAlertsParameters.to_json()

# convert the object into a dict
get_device_alerts_parameters_dict = get_device_alerts_parameters_instance.to_dict()
# create an instance of GetDeviceAlertsParameters from a dict
get_device_alerts_parameters_form_dict = get_device_alerts_parameters.from_dict(get_device_alerts_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


