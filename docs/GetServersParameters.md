# GetServersParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_by** | [**FilterBy8**](FilterBy8.md) |  | [optional] 
**fields** | [**List[ServersFieldsEnum]**](ServersFieldsEnum.md) | Specify which fields to return for each item. See the endpoint description for details of supported fields. | 
**sort_by** | [**List[ValidatingSortClauseservers]**](ValidatingSortClauseservers.md) |  | [optional] [default to [{field=server_name, order=asc}]]
**offset** | **int** | An offset in the data. This can be used to fetch all data in a paginated manner, by e.g requesting (offset&#x3D;0, limit&#x3D;100) followed by (offset&#x3D;100, limit&#x3D;100), (offset&#x3D;200, limit&#x3D;100), etc. | [optional] [default to 0]
**limit** | **int** | Maximum amount of items to fetch | [optional] [default to 100]
**include_count** | **bool** |  | [optional] [default to False]

## Example

```python
from medigate_api.models.get_servers_parameters import GetServersParameters

# TODO update the JSON string below
json = "{}"
# create an instance of GetServersParameters from a JSON string
get_servers_parameters_instance = GetServersParameters.from_json(json)
# print the JSON string representation of the object
print GetServersParameters.to_json()

# convert the object into a dict
get_servers_parameters_dict = get_servers_parameters_instance.to_dict()
# create an instance of GetServersParameters from a dict
get_servers_parameters_form_dict = get_servers_parameters.from_dict(get_servers_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


