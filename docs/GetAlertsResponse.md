# GetAlertsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | **List[object]** |  | 
**count** | **int** |  | [optional] 

## Example

```python
from medigate_api.models.get_alerts_response import GetAlertsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAlertsResponse from a JSON string
get_alerts_response_instance = GetAlertsResponse.from_json(json)
# print the JSON string representation of the object
print GetAlertsResponse.to_json()

# convert the object into a dict
get_alerts_response_dict = get_alerts_response_instance.to_dict()
# create an instance of GetAlertsResponse from a dict
get_alerts_response_form_dict = get_alerts_response.from_dict(get_alerts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


