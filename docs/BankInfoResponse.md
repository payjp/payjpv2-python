# BankInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_code** | **str** | 銀行コード | 
**bank_branch_code** | **str** | 支店番号 | 
**bank_account_type** | **str** | 口座種別 | 
**bank_account_number** | **str** | 口座番号 | 
**bank_account_holder_name** | **str** | 口座名義 | 
**bank_account_status** | **str** | 最新振込結果  | 指定できる値 | |:---| | **success**: 成功 | | **failed**: 失敗 | | **pending**: 初回振込み前 | | 

## Example

```python
from payjpv2.models.bank_info_response import BankInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BankInfoResponse from a JSON string
bank_info_response_instance = BankInfoResponse.from_json(json)
# print the JSON string representation of the object
print(BankInfoResponse.to_json())

# convert the object into a dict
bank_info_response_dict = bank_info_response_instance.to_dict()
# create an instance of BankInfoResponse from a dict
bank_info_response_from_dict = BankInfoResponse.from_dict(bank_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


