import os
import sys
import uuid

import payjpv2

# Get settings from environment variables
api_host = os.environ.get("PAYJP_API_HOST", "https://api.pay.jp")
api_key = os.environ.get("PAYJP_API_KEY", "")

if not api_key:
    print("Error: Please set the PAYJP_API_KEY environment variable", file=sys.stderr)
    sys.exit(1)

# Configure authentication method (Bearer token)
configuration = payjpv2.Configuration(
    host=api_host,
    access_token=api_key,
)

with payjpv2.ApiClient(configuration) as api_client:
    customers_api = payjpv2.CustomersApi(api_client)

    try:
        # 1. Create Customer
        print("=== 1. Create Customer ===")
        create_request = payjpv2.CustomerCreateRequest(
            email="test@example.com",
            description="Test customer from Python SDK",
        )

        idempotency_key = str(uuid.uuid4())
        print(f"Using Idempotency-Key: {idempotency_key}")

        customer = customers_api.create_customer(
            create_request,
            idempotency_key=idempotency_key,
        )
        customer_id = customer.id
        print(f"Created customer: {customer_id}")
        print(f"Email: {customer.email}\n")

        # 2. Get Customer
        print("=== 2. Get Customer ===")
        retrieved = customers_api.get_customer(customer_id)
        print(f"Retrieved customer: {retrieved.id}")
        print(f"Email: {retrieved.email}")
        print(f"Description: {retrieved.description or '(none)'}\n")

        # 3. Update Customer
        print("=== 3. Update Customer ===")
        update_request = payjpv2.CustomerUpdateRequest(
            description="Updated description from Python SDK",
            email="updated@example.com",
        )

        updated = customers_api.update_customer(customer_id, update_request)
        print(f"Updated customer: {updated.id}")
        print(f"New email: {updated.email}")
        print(f"New description: {updated.description or '(none)'}\n")

        # 4. List Customers
        print("=== 4. List Customers ===")
        customer_list = customers_api.get_all_customers(limit=3)
        print(f"Total customers retrieved: {len(customer_list.data)}")
        for c in customer_list.data:
            print(f"  - {c.id} ({c.email or 'no email'})")
        print()

        # 5. Delete Customer
        print("=== 5. Delete Customer ===")
        customers_api.delete_customer(customer_id)
        print(f"Deleted customer: {customer_id}\n")

        print("=== All tests passed! ===")

    except payjpv2.ApiException as e:
        print(f"Exception: {e}")
        sys.exit(1)
