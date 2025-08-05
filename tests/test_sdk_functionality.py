"""
Functional tests for PAY.JP Python SDK.

These tests verify the SDK functionality using the actual generated models
and API structure without making real API calls.
"""
import pytest
from unittest.mock import Mock, patch
import payjpv2
from payjpv2.api.customers_api import CustomersApi
from payjpv2.api.payment_intents_api import PaymentIntentsApi
from payjpv2.models.customer_create_request import CustomerCreateRequest
from payjpv2.models.payment_intent_create_request import PaymentIntentCreateRequest


class TestSDKBasicFunctionality:
    """Test basic SDK functionality."""

    def test_sdk_import(self):
        """Test that all main SDK components can be imported."""
        # Test that main modules are importable
        assert hasattr(payjpv2, 'Configuration')
        assert hasattr(payjpv2, 'ApiClient')
        assert hasattr(payjpv2, 'CustomersApi')
        assert hasattr(payjpv2, 'PaymentIntentsApi')

    def test_configuration_creation(self, api_key):
        """Test configuration creation with various parameters."""
        config = payjpv2.Configuration(
            host="https://api.pay.jp",
            api_key={'APIKeyHeader': api_key},
            api_key_prefix={'APIKeyHeader': 'Bearer'}
        )
        
        assert config.host == "https://api.pay.jp"
        assert config.api_key['APIKeyHeader'] == api_key
        assert config.api_key_prefix['APIKeyHeader'] == 'Bearer'

    def test_api_client_creation(self, configuration):
        """Test API client creation."""
        with payjpv2.ApiClient(configuration) as client:
            assert client.configuration == configuration
            
            # Test that API instances can be created
            customers_api = CustomersApi(client)
            payment_intents_api = PaymentIntentsApi(client)
            
            assert customers_api.api_client == client
            assert payment_intents_api.api_client == client


class TestCustomerOperations:
    """Test customer operations."""

    def test_customer_create_request_basic(self):
        """Test basic customer creation request."""
        request = CustomerCreateRequest(email="test@example.com")
        assert request.email == "test@example.com"

    def test_customer_create_request_with_description(self):
        """Test customer creation with description."""
        request = CustomerCreateRequest(
            email="test@example.com",
            description="Test customer for SDK testing"
        )
        assert request.email == "test@example.com"
        assert request.description == "Test customer for SDK testing"

    def test_customer_create_request_minimal_valid(self):
        """Test that minimal customer request is valid."""
        request = CustomerCreateRequest()
        # Should be able to create request without required fields
        # (validation happens server-side)
        assert request is not None

    def test_customer_api_instantiation(self, api_client):
        """Test customer API instantiation."""
        customers_api = CustomersApi(api_client)
        assert customers_api.api_client == api_client
        
        # Test that API methods exist
        assert hasattr(customers_api, 'create_customer')
        assert hasattr(customers_api, 'get_customer')
        assert hasattr(customers_api, 'get_all_customers')


class TestPaymentIntentOperations:
    """Test payment intent operations."""

    def test_payment_intent_create_request_basic(self):
        """Test basic payment intent creation request."""
        request = PaymentIntentCreateRequest(amount=1000)
        assert request.amount == 1000

    def test_payment_intent_create_request_with_customer(self):
        """Test payment intent creation with customer."""
        request = PaymentIntentCreateRequest(
            amount=1000,
            customer="cus_test123"
        )
        assert request.amount == 1000
        assert request.customer == "cus_test123"

    def test_payment_intent_create_request_with_description(self):
        """Test payment intent creation with description."""
        request = PaymentIntentCreateRequest(
            amount=1500,
            description="Test payment for SDK"
        )
        assert request.amount == 1500
        assert request.description == "Test payment for SDK"

    def test_payment_intent_api_instantiation(self, api_client):
        """Test payment intent API instantiation."""
        payment_intents_api = PaymentIntentsApi(api_client)
        assert payment_intents_api.api_client == api_client
        
        # Test that API methods exist
        assert hasattr(payment_intents_api, 'create_payment_intent')
        assert hasattr(payment_intents_api, 'retrieve_payment_intent')
        assert hasattr(payment_intents_api, 'get_all_payment_intent')


class TestModelSerialization:
    """Test model serialization capabilities."""

    def test_customer_request_serialization(self):
        """Test customer request serialization."""
        request = CustomerCreateRequest(
            email="test@example.com",
            description="Test customer"
        )
        
        # Test string representation
        str_repr = request.to_str()
        assert "test@example.com" in str_repr
        assert "Test customer" in str_repr
        
        # Test JSON serialization
        json_str = request.to_json()
        assert '"email": "test@example.com"' in json_str

    def test_payment_intent_request_serialization(self):
        """Test payment intent request serialization."""
        request = PaymentIntentCreateRequest(
            amount=1000,
            description="Test payment"
        )
        
        str_repr = request.to_str()
        assert "1000" in str_repr
        assert "Test payment" in str_repr
        
        json_str = request.to_json()
        assert '"amount": 1000' in json_str

    def test_model_dict_conversion(self):
        """Test model to dict conversion."""
        request = CustomerCreateRequest(email="test@example.com")
        
        # Test dict conversion using model_dump
        if hasattr(request, 'model_dump'):
            data = request.model_dump()
            assert data["email"] == "test@example.com"


class TestErrorHandlingFunctionality:
    """Test error handling functionality."""

    def test_api_exception_creation(self):
        """Test API exception creation and properties."""
        from payjpv2.rest import ApiException
        
        exc = ApiException(
            status=400,
            reason="Bad Request",
            body='{"error": {"message": "Invalid email"}}'
        )
        
        assert exc.status == 400
        assert exc.reason == "Bad Request"
        assert "Invalid email" in exc.body

    def test_model_validation_flexibility(self):
        """Test that models are flexible with validation."""
        # These should not raise exceptions at model level
        request1 = CustomerCreateRequest(email="")
        assert request1.email == ""
        
        request2 = PaymentIntentCreateRequest(amount=0)
        assert request2.amount == 0
        
        # Test with unusual but potentially valid values
        request3 = PaymentIntentCreateRequest(amount=999999999)
        assert request3.amount == 999999999


class TestAPIClientConfiguration:
    """Test API client configuration and headers."""

    def test_api_client_headers_configuration(self, api_client):
        """Test that API client has proper configuration."""
        # Verify client has configuration
        assert api_client.configuration is not None
        assert hasattr(api_client.configuration, 'api_key')
        assert hasattr(api_client.configuration, 'host')

    def test_multiple_api_instances(self, api_client):
        """Test that multiple API instances can be created."""
        customers_api = CustomersApi(api_client)
        payment_intents_api = PaymentIntentsApi(api_client)
        
        # Both should share the same client
        assert customers_api.api_client == payment_intents_api.api_client
        assert customers_api.api_client == api_client

    def test_api_client_context_manager_behavior(self, configuration):
        """Test API client context manager behavior."""
        # Test that context manager works properly
        with payjpv2.ApiClient(configuration) as client:
            assert client is not None
            customers_api = CustomersApi(client)
            assert customers_api.api_client == client


class TestWorkflowIntegration:
    """Test workflow integration without actual API calls."""

    def test_customer_workflow_simulation(self, api_client):
        """Test customer workflow simulation."""
        customers_api = CustomersApi(api_client)
        
        # Test creating request objects for workflow
        create_request = CustomerCreateRequest(
            email="workflow@example.com",
            description="Workflow test customer"
        )
        
        assert create_request.email == "workflow@example.com"
        assert create_request.description == "Workflow test customer"
        
        # Verify API object can handle the request structure
        assert hasattr(customers_api, 'create_customer')

    def test_payment_intent_workflow_simulation(self, api_client):
        """Test payment intent workflow simulation."""
        payment_intents_api = PaymentIntentsApi(api_client)
        
        # Test creating request objects for workflow
        create_request = PaymentIntentCreateRequest(
            amount=2500,
            customer="cus_workflow_test",
            description="Workflow test payment"
        )
        
        assert create_request.amount == 2500
        assert create_request.customer == "cus_workflow_test"
        assert create_request.description == "Workflow test payment"
        
        # Verify API object can handle the request structure
        assert hasattr(payment_intents_api, 'create_payment_intent')
        assert hasattr(payment_intents_api, 'retrieve_payment_intent')

    def test_multi_api_coordination(self, api_client):
        """Test coordination between multiple APIs."""
        customers_api = CustomersApi(api_client)
        payment_intents_api = PaymentIntentsApi(api_client)
        
        # Test that both APIs can work with the same client
        assert customers_api.api_client == payment_intents_api.api_client
        
        # Test creating related objects
        customer_request = CustomerCreateRequest(email="coordination@example.com")
        payment_request = PaymentIntentCreateRequest(
            amount=1500,
            customer="cus_coordination_test"
        )
        
        assert customer_request.email == "coordination@example.com"
        assert payment_request.customer == "cus_coordination_test"


class TestSDKStructure:
    """Test SDK structure and organization."""

    def test_api_module_structure(self):
        """Test API module structure."""
        # Test that API classes are properly organized
        from payjpv2.api import customers_api
        from payjpv2.api import payment_intents_api
        
        assert hasattr(customers_api, 'CustomersApi')
        assert hasattr(payment_intents_api, 'PaymentIntentsApi')

    def test_model_module_structure(self):
        """Test model module structure."""
        # Test that model classes are properly organized
        from payjpv2.models import customer_create_request
        from payjpv2.models import payment_intent_create_request
        
        assert hasattr(customer_create_request, 'CustomerCreateRequest')
        assert hasattr(payment_intent_create_request, 'PaymentIntentCreateRequest')

    def test_configuration_accessibility(self):
        """Test configuration accessibility."""
        # Test that configuration is accessible from main module
        assert hasattr(payjpv2, 'Configuration')
        
        # Test configuration creation
        config = payjpv2.Configuration()
        assert config is not None

    def test_exception_accessibility(self):
        """Test exception accessibility."""
        # Test that exceptions are accessible
        from payjpv2.rest import ApiException
        from payjpv2 import exceptions
        
        assert ApiException is not None
        assert exceptions is not None