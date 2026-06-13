# OperandsInner2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of field to filter | 
**operation** | [**CompoundQueryFilterOperation**](CompoundQueryFilterOperation.md) | Operation that is applied to join &#x60;operands&#x60; together | 
**value** | **object** |  | [optional] 
**operands** | [**List[OperandsInner2]**](OperandsInner2.md) | Other filters to join together using &#x60;operation&#x60; | 

## Example

```python
from medigate_api.models.operands_inner2 import OperandsInner2

# TODO update the JSON string below
json = "{}"
# create an instance of OperandsInner2 from a JSON string
operands_inner2_instance = OperandsInner2.from_json(json)
# print the JSON string representation of the object
print(OperandsInner2.to_json())

# convert the object into a dict
operands_inner2_dict = operands_inner2_instance.to_dict()
# create an instance of OperandsInner2 from a dict
operands_inner2_from_dict = OperandsInner2.from_dict(operands_inner2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


