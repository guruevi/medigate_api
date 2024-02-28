# SetVulnerabilitiesRelevanceParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vulnerabilities** | [**VulnerabilitiesFilterBy**](VulnerabilitiesFilterBy.md) |  | 
**devices** | [**DevicesFilterBy**](DevicesFilterBy.md) |  | [optional] 
**relevance** | [**VulnerabilityRelevance**](VulnerabilityRelevance.md) |  | 

## Example

```python
from medigate_api.models.set_vulnerabilities_relevance_params import SetVulnerabilitiesRelevanceParams

# TODO update the JSON string below
json = "{}"
# create an instance of SetVulnerabilitiesRelevanceParams from a JSON string
set_vulnerabilities_relevance_params_instance = SetVulnerabilitiesRelevanceParams.from_json(json)
# print the JSON string representation of the object
print SetVulnerabilitiesRelevanceParams.to_json()

# convert the object into a dict
set_vulnerabilities_relevance_params_dict = set_vulnerabilities_relevance_params_instance.to_dict()
# create an instance of SetVulnerabilitiesRelevanceParams from a dict
set_vulnerabilities_relevance_params_form_dict = set_vulnerabilities_relevance_params.from_dict(set_vulnerabilities_relevance_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


