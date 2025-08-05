"""
Tests for PAY.JP SDK model validation and serialization.
"""
import pytest
from payjpv2.models.customer_create_request import CustomerCreateRequest
from payjpv2.models.payment_intent_create_request import PaymentIntentCreateRequest


class TestCustomerModels:
    """Test customer-related models."""

    def test_customer_create_request_basic(self):
        """Test basic customer creation request."""
        request = CustomerCreateRequest()
        assert request is not None

    def test_customer_create_request_with_email(self):
        """Test customer creation request with email."""
        request = CustomerCreateRequest(email="test@example.com")
        assert request.email == "test@example.com"

    def test_customer_create_request_with_description(self):
        """Test customer creation with description."""
        request = CustomerCreateRequest(
            email="test@example.com",
            description="Test customer"
        )
        assert request.email == "test@example.com"
        assert request.description == "Test customer"

    def test_customer_create_request_minimal_valid(self):
        """Test that minimal customer request is valid."""
        request = CustomerCreateRequest()
        assert request is not None


class TestPaymentIntentModels:
    """Test payment intent-related models."""

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

    def test_payment_intent_amount_types(self):
        """Test different amount values."""
        # Positive amount
        request1 = PaymentIntentCreateRequest(amount=1000)
        assert request1.amount == 1000
        
        # Zero amount (may be valid for some use cases)
        request2 = PaymentIntentCreateRequest(amount=0)
        assert request2.amount == 0
        
        # Large amount
        request3 = PaymentIntentCreateRequest(amount=999999999)
        assert request3.amount == 999999999

    def test_payment_intent_capture_method(self):
        """Test capture method settings if available."""
        # Test that capture_method field exists and can be set
        request = PaymentIntentCreateRequest(amount=1000)
        if hasattr(request, 'capture_method'):
            # Only test if the field exists in this implementation
            assert request.capture_method is None  # Default value


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
        
        # Test dict conversion using model_dump if available
        if hasattr(request, 'model_dump'):
            data = request.model_dump()
            assert data["email"] == "test@example.com"


class TestModelValidation:
    """Test model validation flexibility."""

    def test_email_format_flexibility(self):
        """Test that email format is flexible at model level."""
        # These should all be accepted at model level
        emails = [
            "test@example.com",
            "test+tag@example.com", 
            "test.user@example.co.jp",
            "invalid-email",  # Let server validate
            ""
        ]
        
        for email in emails:
            request = CustomerCreateRequest(email=email)
            assert request.email == email

    def test_amount_flexibility(self):
        """Test that amount validation is flexible."""
        amounts = [1, 100, 1000, 999999999, 0]
        
        for amount in amounts:
            request = PaymentIntentCreateRequest(amount=amount)
            assert request.amount == amount

    def test_model_optional_fields(self):
        """Test that optional fields work correctly."""
        # Test customer with just email
        customer_request = CustomerCreateRequest(email="test@example.com")
        assert customer_request.email == "test@example.com"
        assert customer_request.description is None
        
        # Test payment intent with just amount
        payment_request = PaymentIntentCreateRequest(amount=1000)
        assert payment_request.amount == 1000
        assert payment_request.customer is None