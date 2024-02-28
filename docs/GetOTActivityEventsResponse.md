# GetOTActivityEventsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ot_activity_events** | **List[object]** |  | 
**count** | **int** |  | [optional] 

## Example

```python
from medigate_api.models.get_ot_activity_events_response import GetOTActivityEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOTActivityEventsResponse from a JSON string
get_ot_activity_events_response_instance = GetOTActivityEventsResponse.from_json(json)
# print the JSON string representation of the object
print GetOTActivityEventsResponse.to_json()

# convert the object into a dict
get_ot_activity_events_response_dict = get_ot_activity_events_response_instance.to_dict()
# create an instance of GetOTActivityEventsResponse from a dict
get_ot_activity_events_response_form_dict = get_ot_activity_events_response.from_dict(get_ot_activity_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


