# SetupFlowCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | この SetupFlow が属する顧客の ID。SetupFlow に PaymentMethod が設定されている場合、SetupFlow の設定が成功するとその PaymentMethod は顧客に紐付きます。別の顧客に紐付いている PaymentMethod をこの SetupFlow で使用することはできません。 | [optional] 
**description** | **str** | 説明。顧客に表示されます。 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 
**payment_method_options** | [**SetupFlowPaymentMethodOptionsRequest**](SetupFlowPaymentMethodOptionsRequest.md) | この SetupFlow の支払い方法の個別設定。 | [optional] 
**payment_method_types** | **List[str]** | この SetupFlow で使用できる支払い方法の種類（カードなど）のリストです。 指定しない場合、ダッシュボードで利用可能な状態にしている支払い方法が自動的に設定されます。 | [optional] 
**usage** | [**Usage**](Usage.md) | 支払い方法が今後どのように使用されるかを指定します。指定されていない場合、この値はデフォルトで &#x60;off_session&#x60; になります。  | 指定できる値 | |:---| | **off_session**: 定期課金など、顧客がカートなどの決済フローにいるかどうか不明な場合は &#x60;off_session&#x60; を使用してください。 | | **on_session**: 顧客がカートなどの決済フローにいる場合にのみ支払い方法を利用する場合は &#x60;on_session&#x60; を使用してください。 | | [optional] 

## Example

```python
from payjpv2.models.setup_flow_create_request import SetupFlowCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetupFlowCreateRequest from a JSON string
setup_flow_create_request_instance = SetupFlowCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SetupFlowCreateRequest.to_json())

# convert the object into a dict
setup_flow_create_request_dict = setup_flow_create_request_instance.to_dict()
# create an instance of SetupFlowCreateRequest from a dict
setup_flow_create_request_from_dict = SetupFlowCreateRequest.from_dict(setup_flow_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


