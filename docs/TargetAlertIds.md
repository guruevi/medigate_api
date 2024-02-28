# TargetAlertIds


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_ids** | **List[int]** | A list of Alert IDs, as indicated in the &#x60;id&#x60; field of an alert. | 

## Example

```python
from medigate_api.models.target_alert_ids import TargetAlertIds

# TODO update the JSON string below
json = "{}"
# create an instance of TargetAlertIds from a JSON string
target_alert_ids_instance = TargetAlertIds.from_json(json)
# print the JSON string representation of the object
print TargetAlertIds.to_json()

# convert the object into a dict
target_alert_ids_dict = target_alert_ids_instance.to_dict()
# create an instance of TargetAlertIds from a dict
target_alert_ids_form_dict = target_alert_ids.from_dict(target_alert_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


