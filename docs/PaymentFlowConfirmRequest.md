# PaymentFlowConfirmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | 支払い方法ID | [optional] 
**payment_method_options** | [**PaymentMethodOptionsRequest**](PaymentMethodOptionsRequest.md) | このPaymentFlowに固有の支払い方法の設定 | [optional] 
**payment_method_types** | [**List[PaymentMethodTypes]**](PaymentMethodTypes.md) | このPaymentFlowで使用できる支払い方法の種類（カードなど）のリストです。 指定しない場合は、PAY.JPは支払い方法の設定から利用可能な支払い方法を動的に表示します。 | [optional] 
**return_url** | **str** | 顧客が支払いを完了後かキャンセルした後にリダイレクトされるURL。アプリにリダイレクトしたい場合は URI Scheme を指定できます。confirm&#x3D;trueの場合のみ指定できます。 | [optional] 
**description** | **str** | オブジェクトにセットする任意の文字列。ユーザーには表示されません。 | [optional] 
**capture_method** | [**CaptureMethod**](CaptureMethod.md) | 支払いの確定方法を指定します。  | 指定できる値 | |:---| | **automatic**: (デフォルト) 顧客が支払いを承認すると、自動的に確定させます。 | | **manual**: 顧客が支払いを承認すると一旦確定を保留し、後で Capture API を使用して確定します。（すべての支払い方法がこれをサポートしているわけではありません）。 | | [optional] 

## Example

```python
from payjpv2.models.payment_flow_confirm_request import PaymentFlowConfirmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowConfirmRequest from a JSON string
payment_flow_confirm_request_instance = PaymentFlowConfirmRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowConfirmRequest.to_json())

# convert the object into a dict
payment_flow_confirm_request_dict = payment_flow_confirm_request_instance.to_dict()
# create an instance of PaymentFlowConfirmRequest from a dict
payment_flow_confirm_request_from_dict = PaymentFlowConfirmRequest.from_dict(payment_flow_confirm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


