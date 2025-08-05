from pprint import pprint

import payjpv2
import payjpv2.rest

# PAY.JPのAPIキー（環境変数から取得）
import os
api_key = os.environ.get("PAYJP_API_KEY", "sk_test_c62fade9d045b54cd76d7036")

# 認証方式の設定
# APIKeyHeader は PAY.JPが使用している認証スキーム名
configuration = payjpv2.Configuration(
    host = "http://localhost:8200",
    api_key = {'APIKeyHeader': api_key},
    api_key_prefix = {'APIKeyHeader': 'Bearer'}
)

with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.CustomersApi(api_client)
    customer_create_request = payjpv2.CustomerCreateRequest(
        email="jennyrosen@example.com",
    )

    try:
        # Create Checkout Session
        api_response = api_instance.create_customer(customer_create_request)
        print("The response of->create_customer:\n")
        pprint(api_response)
    except payjpv2.rest.ApiException as e:
        print("Exception when calling CustomersApi->create_customer: %s\n" % e)
