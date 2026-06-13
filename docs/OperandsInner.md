# OperandsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of field to filter | 
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**value** | **object** |  | [optional] 
**operands** | [**List[OperandsInner]**](OperandsInner.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.operands_inner import OperandsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OperandsInner from a JSON string
operands_inner_instance = OperandsInner.from_json(json)
# print the JSON string representation of the object
print(OperandsInner.to_json())

# convert the object into a dict
operands_inner_dict = operands_inner_instance.to_dict()
# create an instance of OperandsInner from a dict
operands_inner_from_dict = OperandsInner.from_dict(operands_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


