# PaymentFlowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 支払いインテントID | 
**object** | **str** |  | [optional] [default to 'payment_flow']
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | 
**livemode** | **bool** | 本番環境かどうか | 
**amount** | **int** | 支払い予定の金額。50円以上9,999,999円以下である必要があります。支払い手段によって上限金額は異なります。 | 
**amount_capturable** | **int** |  | 
**amount_received** | **int** |  | 
**client_secret** | **str** | このPaymentFlowのクライアントシークレットです。フロントエンドで公開APIキーと合わせて使用しPaymentFlowの情報を取得や支払い処理を行います。**この値はこのPaymentFlowの支払いを行う顧客以外へ公開しないでください。**また保存やログへの記録なども行わないでください。 | 
**confirmation_method** | **str** |  | 
**customer** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | [optional] 
**payment_method** | **str** |  | [optional] 
**payment_method_options** | **Dict[str, object]** |  | [optional] 
**payment_method_types** | **List[str]** | このPaymentFlowで使用できる支払い方法の種類（カードなど）のリストです。 指定しない場合は、PAY.JPは支払い方法の設定から利用可能な支払い方法を動的に表示します。 | 
**receipt_email** | **str** |  | [optional] 
**status** | [**PaymentFlowStatus**](PaymentFlowStatus.md) | このPaymentFlowのステータスです。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/payment_flows#status\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ステータスの詳細についてはこちらをご覧ください。&lt;/a&gt;  | 値 | |:---| | **requires_payment_method**: 支払い方法が必要です。 | | **requires_confirmation**: 確認が必要です。 | | **requires_action**: 顧客のアクションが必要です。 | | **processing**: 処理中です。 | | **requires_capture**: 確定が必要です。 | | **canceled**: キャンセルされました。 | | **succeeded**: 成功しました。 | | 
**next_action** | **Dict[str, object]** |  | [optional] 
**return_url** | **str** |  | [optional] 
**capture_method** | [**CaptureMethod**](CaptureMethod.md) | 支払いの確定方法を指定します。  | 指定できる値 | |:---| | **automatic**: (デフォルト) 顧客が支払いを承認すると、自動的に確定させます。 | | **manual**: 顧客が支払いを承認すると一旦確定を保留し、後で Capture API を使用して確定します。（すべての支払い方法がこれをサポートしているわけではありません）。 | | 
**last_payment_error** | **Dict[str, object]** |  | 

## Example

```python
from payjpv2.models.payment_flow_response import PaymentFlowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowResponse from a JSON string
payment_flow_response_instance = PaymentFlowResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowResponse.to_json())

# convert the object into a dict
payment_flow_response_dict = payment_flow_response_instance.to_dict()
# create an instance of PaymentFlowResponse from a dict
payment_flow_response_from_dict = PaymentFlowResponse.from_dict(payment_flow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


