# OperandsInner3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of field to filter | 
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**value** | **object** |  | [optional] 
**operands** | [**List[OperandsInner3]**](OperandsInner3.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.operands_inner3 import OperandsInner3

# TODO update the JSON string below
json = "{}"
# create an instance of OperandsInner3 from a JSON string
operands_inner3_instance = OperandsInner3.from_json(json)
# print the JSON string representation of the object
print(OperandsInner3.to_json())

# convert the object into a dict
operands_inner3_dict = operands_inner3_instance.to_dict()
# create an instance of OperandsInner3 from a dict
operands_inner3_from_dict = OperandsInner3.from_dict(operands_inner3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


