# StatementResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'statement']
**id** | **str** | 明細ID | 
**livemode** | **bool** | 本番環境かどうか | 
**title** | **str** |  | [optional] 
**type** | [**StatementType**](StatementType.md) | 取引明細の区分  | 名 | 区分 | 詳細 | |---| --- | --- | | **sales** | 売上 | 決済による売上、決済手数料等 | | **service_fee** | サービス利用料 | 有料プランの月額費用など、salesに含まれないサービス利用料 | | **forfeit** | 残高失効 | - | | **transfer_fee** | 振込手数料 | - | | **misc** | その他 | 調整金など | | 
**created_at** | **datetime** | 更新時の日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新時の日時 (UTC, ISO 8601 形式) | 
**tenant** | **str** |  | [optional] 
**term** | [**TermResponse**](TermResponse.md) |  | [optional] 
**balance** | **str** |  | [optional] 
**items** | [**List[StatementItemResponse]**](StatementItemResponse.md) | 明細項目のリスト | 
**net** | **int** | 含まれるstatement_itemの金額合計 | 

## Example

```python
from payjpv2.models.statement_response import StatementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatementResponse from a JSON string
statement_response_instance = StatementResponse.from_json(json)
# print the JSON string representation of the object
print(StatementResponse.to_json())

# convert the object into a dict
statement_response_dict = statement_response_instance.to_dict()
# create an instance of StatementResponse from a dict
statement_response_from_dict = StatementResponse.from_dict(statement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


