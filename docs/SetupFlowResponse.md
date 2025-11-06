# SetupFlowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | 
**object** | **str** |  | [optional] [default to 'setup_flow']
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | 
**livemode** | **bool** | 本番環境かどうか | 
**client_secret** | **str** | この SetupFlow のクライアントシークレットです。フロントエンドで公開鍵と合わせて使用し、SetupFlow の取得や支払い処理を行います。**この値はこの SetupFlow の支払いを行う顧客以外へ公開しないでください。 | 
**customer** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | [optional] 
**payment_method** | **str** |  | [optional] 
**payment_method_options** | **Dict[str, object]** |  | [optional] 
**payment_method_types** | **List[str]** | この SetupFlow で使用できる支払い方法の種類（カードなど）のリストです。 指定しない場合、ダッシュボードで利用可能な状態にしている支払い方法が自動的に設定されます。 | 
**status** | [**SetupFlowStatus**](SetupFlowStatus.md) | この SetupFlow のステータスです。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/setup_flows#status\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ステータスの詳細についてはこちらをご覧ください。&lt;/a&gt;  | 値 | |:---| | **requires_payment_method**: 支払い方法が必要です。 | | **requires_confirmation**: 確認が必要です。 | | **requires_action**: 顧客のアクションが必要です。 | | **processing**: 処理中です。 | | **succeeded**: 成功しました。 | | **canceled**: キャンセルされました。 | | 
**next_action** | **Dict[str, object]** |  | [optional] 
**return_url** | **str** |  | [optional] 
**last_setup_error** | **Dict[str, object]** |  | 

## Example

```python
from payjpv2.models.setup_flow_response import SetupFlowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetupFlowResponse from a JSON string
setup_flow_response_instance = SetupFlowResponse.from_json(json)
# print the JSON string representation of the object
print(SetupFlowResponse.to_json())

# convert the object into a dict
setup_flow_response_dict = setup_flow_response_instance.to_dict()
# create an instance of SetupFlowResponse from a dict
setup_flow_response_from_dict = SetupFlowResponse.from_dict(setup_flow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


