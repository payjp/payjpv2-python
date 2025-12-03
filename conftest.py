"""
Pytest configuration and fixtures for PAY.JP Python SDK tests.
"""
import os
from unittest.mock import Mock, patch

import pytest

import payjpv2
from payjpv2.api_client import ApiClient
from payjpv2.configuration import Configuration


@pytest.fixture
def api_key():
    """Test API key fixture."""
    return "sk_test_example_api_key"


@pytest.fixture
def configuration(api_key):
    """Test configuration fixture."""
    config = Configuration(
        host="https://api.pay.jp",
        api_key={'APIKeyHeader': api_key},
        api_key_prefix={'APIKeyHeader': 'Bearer'}
    )
    return config


@pytest.fixture
def api_client(configuration):
    """Test API client fixture."""
    return ApiClient(configuration)


@pytest.fixture
def mock_api_response():
    """Mock API response fixture."""
    mock_response = Mock()
    mock_response.status = 200
    mock_response.reason = "OK"
    mock_response.data = b'{"id": "test_id", "object": "test_object"}'
    mock_response.headers = {"Content-Type": "application/json"}
    return mock_response


@pytest.fixture
def sample_customer_data():
    """Sample customer data for testing."""
    return {
        "id": "cus_test123",
        "object": "customer",
        "email": "test@example.com",
        "created": 1234567890,
        "livemode": False,
        "metadata": {}
    }


@pytest.fixture
def sample_payment_flow_data():
    """Sample payment flow data for testing."""
    return {
        "id": "pfw_test123",
        "object": "payment_flow",
        "amount": 1000,
        "currency": "jpy",
        "status": "requires_payment_method",
        "created": 1234567890,
        "livemode": False,
        "metadata": {}
    }


@pytest.fixture
def sample_payment_method_data():
    """Sample payment method data for testing."""
    return {
        "id": "pm_test123",
        "object": "payment_method",
        "type": "card",
        "card": {
            "brand": "visa",
            "last4": "4242",
            "exp_month": 12,
            "exp_year": 2025
        },
        "created": 1234567890,
        "livemode": False
    }


@pytest.fixture
def env_vars():
    """Environment variables fixture."""
    with patch.dict(os.environ, {
        'PAYJP_API_KEY': 'sk_test_example_api_key',
        'PAYJP_API_HOST': 'https://api.pay.jp'
    }):
        yield


@pytest.fixture(autouse=True)
def reset_configuration():
    """Reset configuration after each test."""
    yield
    # Reset any global configuration if needed