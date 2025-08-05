# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Testing Commands
- `python -m pytest` - Run all tests (both auto-generated and hand-written)
- `pytest tests/` - Run only hand-written tests in tests/ directory
- `pytest test/` - Run auto-generated tests in test/ directory
- `pytest tests/test_simple_functionality.py tests/test_configuration.py tests/test_error_handling.py tests/test_integration.py -v` - Run working test modules with verbose output
- `pytest --cov=payjpv2 --cov-report=term-missing --cov-report=html` - Run tests with coverage report
- `tox` - Run tests across multiple Python environments

### Code Quality Commands
- `ruff check` - Run Python linting
- `mypy payjpv2/` - Run type checking on main package
- `mypy tests/` - Run type checking on hand-written tests

### Package Management
- `pip install -r requirements.txt` - Install runtime dependencies
- `pip install -r test-requirements.txt` - Install test dependencies
- `python setup.py install --user` - Install package locally

## Architecture

This is the **Python SDK** component of a multi-language SDK generator for the PAY.JP v2 API. The Python SDK is auto-generated from an OpenAPI specification using openapi-generator with custom templates.

### Core Structure
- **Package Name**: `payjpv2` - Main Python package containing all SDK components
- **Generated Code**: Most code is auto-generated and should not be edited directly
- **Custom Tests**: Hand-written tests in `tests/` directory complement auto-generated tests in `test/`

### Key Components
- **API Clients**: Located in `payjpv2/api/` - One client class per API resource (e.g., PaymentIntentsApi, CustomersApi)
- **Models**: Located in `payjpv2/models/` - Pydantic-based data models for requests and responses
- **Core Client**: `payjpv2/api_client.py` - Main HTTP client with authentication and request handling
- **Configuration**: `payjpv2/configuration.py` - SDK configuration including API keys and endpoints
- **Exceptions**: `payjpv2/exceptions.py` - Custom exception classes for API errors

### Code Generation Context
- **Auto-generated files**: All files in `payjpv2/` directory are generated from OpenAPI spec
- **Template customization**: Generation behavior is controlled by templates in parent directory's `templates/python/` 
- **Package metadata**: Controlled via Makefile variables in parent directory
- **Version management**: Package version is set during generation process

### Test Structure
The SDK has two parallel test suites:
1. **Auto-generated tests** (`test/` directory): Generated model and API tests
2. **Hand-written tests** (`tests/` directory): Integration, configuration, and functionality tests

### Important Testing Notes
- Current working tests are in `tests/` directory (test_simple_functionality.py, test_configuration.py, test_error_handling.py, test_integration.py)
- Auto-generated tests in `test/` directory may have issues and should be verified before use
- Test configuration uses pytest with coverage reporting and specific markers for test categorization
- All tests use mocking to avoid real API calls

### Key Dependencies
- **Pydantic v2**: Used for data validation and serialization in models
- **urllib3**: HTTP client library for API requests
- **python-dateutil**: Date/time handling utilities
- **typing-extensions**: Enhanced type hints support

### Development Workflow
1. **Never edit generated code**: All files in `payjpv2/` are auto-generated
2. **Add custom tests**: Place new tests in `tests/` directory
3. **Follow existing patterns**: Use established test fixtures and mocking strategies
4. **Check code quality**: Run ruff and mypy before committing changes
5. **Verify test coverage**: Maintain coverage above 80% threshold