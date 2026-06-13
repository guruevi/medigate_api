# OperandsInner6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of field to filter | 
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**value** | **object** |  | [optional] 
**operands** | [**List[OperandsInner6]**](OperandsInner6.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.operands_inner6 import OperandsInner6

# TODO update the JSON string below
json = "{}"
# create an instance of OperandsInner6 from a JSON string
operands_inner6_instance = OperandsInner6.from_json(json)
# print the JSON string representation of the object
print(OperandsInner6.to_json())

# convert the object into a dict
operands_inner6_dict = operands_inner6_instance.to_dict()
# create an instance of OperandsInner6 from a dict
operands_inner6_from_dict = OperandsInner6.from_dict(operands_inner6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


