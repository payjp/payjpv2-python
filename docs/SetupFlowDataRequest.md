# SetupFlowDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 

## Example

```python
from payjpv2.models.setup_flow_data_request import SetupFlowDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetupFlowDataRequest from a JSON string
setup_flow_data_request_instance = SetupFlowDataRequest.from_json(json)
# print the JSON string representation of the object
print(SetupFlowDataRequest.to_json())

# convert the object into a dict
setup_flow_data_request_dict = setup_flow_data_request_instance.to_dict()
# create an instance of SetupFlowDataRequest from a dict
setup_flow_data_request_from_dict = SetupFlowDataRequest.from_dict(setup_flow_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


