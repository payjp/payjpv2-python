# BalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'balance']
**id** | **str** | 残高ID | 
**livemode** | **bool** | 本番環境かどうか | 
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新時の日時 (UTC, ISO 8601 形式) | 
**state** | [**BalanceState**](BalanceState.md) | Balanceの状態  | 指定できる値 | |:---| | **collecting**: 集計中 | | **transfer**: 入金 | | **claim**: 請求 | | 
**statements** | [**List[StatementResponse]**](StatementResponse.md) | 関連付けられているStatementオブジェクトのリスト | 
**closed** | **bool** | このBalanceの清算が終了していればtrue  state&#x3D;transferであれば加盟店口座への入金作業完了、state&#x3D;claimであればPAY.JPで請求額の振込が確認できたことを表します。 | 
**closed_date** | **datetime** |  | 
**due_date** | **datetime** |  | 
**net** | **int** | 関連付けられているStatementの総額 | 
**bank_info** | [**BankInfoResponse**](BankInfoResponse.md) |  | 

## Example

```python
from payjpv2.models.balance_response import BalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceResponse from a JSON string
balance_response_instance = BalanceResponse.from_json(json)
# print the JSON string representation of the object
print(BalanceResponse.to_json())

# convert the object into a dict
balance_response_dict = balance_response_instance.to_dict()
# create an instance of BalanceResponse from a dict
balance_response_from_dict = BalanceResponse.from_dict(balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


