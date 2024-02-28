# GetOTActivityEventsParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_by** | [**FilterBy6**](FilterBy6.md) |  | [optional] 
**fields** | [**List[PublicOtActivityEventsFieldsEnum]**](PublicOtActivityEventsFieldsEnum.md) | Specify which fields to return for each item. See the endpoint description for details of supported fields. | 
**sort_by** | [**List[ValidatingSortClausepublicOtActivityEvents]**](ValidatingSortClausepublicOtActivityEvents.md) |  | [optional] [default to [{field=event_id, order=asc}]]
**offset** | **int** | An offset in the data. This can be used to fetch all data in a paginated manner, by e.g requesting (offset&#x3D;0, limit&#x3D;100) followed by (offset&#x3D;100, limit&#x3D;100), (offset&#x3D;200, limit&#x3D;100), etc. | [optional] [default to 0]
**limit** | **int** | Maximum amount of items to fetch | [optional] [default to 100]
**include_count** | **bool** |  | [optional] [default to False]

## Example

```python
from medigate_api.models.get_ot_activity_events_parameters import GetOTActivityEventsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of GetOTActivityEventsParameters from a JSON string
get_ot_activity_events_parameters_instance = GetOTActivityEventsParameters.from_json(json)
# print the JSON string representation of the object
print GetOTActivityEventsParameters.to_json()

# convert the object into a dict
get_ot_activity_events_parameters_dict = get_ot_activity_events_parameters_instance.to_dict()
# create an instance of GetOTActivityEventsParameters from a dict
get_ot_activity_events_parameters_form_dict = get_ot_activity_events_parameters.from_dict(get_ot_activity_events_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


