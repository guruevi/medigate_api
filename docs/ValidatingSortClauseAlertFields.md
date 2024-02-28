# ValidatingSortClauseAlertFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | [**AlertFieldsSortableFieldsEnum**](AlertFieldsSortableFieldsEnum.md) | Name of field to sort by | 
**order** | [**SortOrder**](SortOrder.md) | Direction of sort | 

## Example

```python
from medigate_api.models.validating_sort_clause_alert_fields import ValidatingSortClauseAlertFields

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingSortClauseAlertFields from a JSON string
validating_sort_clause_alert_fields_instance = ValidatingSortClauseAlertFields.from_json(json)
# print the JSON string representation of the object
print ValidatingSortClauseAlertFields.to_json()

# convert the object into a dict
validating_sort_clause_alert_fields_dict = validating_sort_clause_alert_fields_instance.to_dict()
# create an instance of ValidatingSortClauseAlertFields from a dict
validating_sort_clause_alert_fields_form_dict = validating_sort_clause_alert_fields.from_dict(validating_sort_clause_alert_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


