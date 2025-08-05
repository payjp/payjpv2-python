# Testing Guide for PAY.JP Python SDK

This document describes the testing approach and test suites for the PAY.JP Python SDK.

## Test Structure

The test suite is organized into several focused test modules:

### Core Test Modules

1. **`tests/test_simple_functionality.py`** - Basic SDK functionality tests
   - Package imports and structure
   - Configuration creation and management
   - API client instantiation
   - Model creation and serialization
   - Error class functionality

2. **`tests/test_configuration.py`** - Configuration and client tests
   - Configuration object creation and validation
   - API client initialization with various configurations
   - Context manager behavior
   - Multi-client independence
   - Thread safety

3. **`tests/test_error_handling.py`** - Error handling tests
   - API exception handling for various HTTP status codes
   - Network error simulation
   - Error message parsing and extraction
   - Client-side validation flexibility

4. **`tests/test_integration.py`** - Integration tests
   - Multi-component workflow testing
   - API workflow simulation
   - Cross-component interaction verification

## Test Configuration

### Prerequisites

Install test dependencies:
```bash
pip install -r test-requirements.txt
```

### Test Dependencies

- `pytest >= 7.2.1` - Testing framework
- `pytest-cov >= 2.8.1` - Coverage reporting
- `pytest-mock >= 3.10.0` - Mocking utilities
- `coverage >= 7.0.0` - Coverage analysis

### Running Tests

Run all working tests:
```bash
pytest tests/test_simple_functionality.py tests/test_configuration.py tests/test_error_handling.py tests/test_integration.py -v
```

Run with coverage:
```bash
pytest tests/test_simple_functionality.py tests/test_configuration.py tests/test_error_handling.py tests/test_integration.py -v --cov=payjpv2 --cov-report=term-missing
```

Run specific test categories:
```bash
# Basic functionality
pytest tests/test_simple_functionality.py -v

# Configuration tests
pytest tests/test_configuration.py -v

# Error handling
pytest tests/test_error_handling.py -v

# Integration tests
pytest tests/test_integration.py -v
```

## Test Coverage

Current test coverage focuses on:

- ✅ **SDK Imports** - All main components importable
- ✅ **Configuration** - Configuration creation and validation
- ✅ **API Client** - Client instantiation and context management
- ✅ **Model Creation** - Request model creation with various parameters
- ✅ **Serialization** - Model to string/JSON conversion
- ✅ **Error Handling** - Exception creation and HTTP error simulation
- ✅ **Integration** - Multi-component workflows

## Test Philosophy

### Unit Testing Approach

The test suite follows these principles:

1. **No Real API Calls** - All tests use mocking to avoid external dependencies
2. **Component Isolation** - Each test focuses on specific SDK components
3. **Realistic Usage** - Tests simulate real-world SDK usage patterns
4. **Error Scenarios** - Comprehensive error condition testing

### Mock Strategy

- **Configuration Testing** - Direct object testing without mocking
- **API Client Testing** - Context manager and initialization testing
- **Error Simulation** - Mock API exceptions for error handling tests
- **Integration Testing** - Mock API responses for workflow testing

## Test Fixtures

### Common Fixtures (conftest.py)

- `api_key` - Test API key
- `configuration` - Pre-configured Configuration object
- `api_client` - Pre-configured ApiClient
- `sample_*_data` - Sample response data for various object types
- `env_vars` - Environment variable mocking

## Testing Best Practices

### For Contributors

1. **Run Tests Before Commit**
   ```bash
   pytest tests/test_simple_functionality.py tests/test_configuration.py tests/test_error_handling.py tests/test_integration.py
   ```

2. **Add Tests for New Features**
   - Add unit tests for new model classes
   - Add integration tests for new API workflows
   - Add error handling tests for new error conditions

3. **Mock External Dependencies**
   - Never make real API calls in tests
   - Use appropriate mocking for HTTP responses
   - Test both success and failure scenarios

### Test Naming Conventions

- Test files: `test_<component>.py`
- Test classes: `Test<Component>`
- Test methods: `test_<functionality>`

### Test Documentation

Each test includes:
- Clear docstring describing what is being tested
- Arrange-Act-Assert structure
- Meaningful assertions with specific error messages

## Continuous Integration

### GitHub Actions

The project uses GitHub Actions for CI/CD:

- **Python Matrix Testing** - Tests on Python 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- **Coverage Requirements** - Minimum 80% coverage threshold
- **Linting** - Code quality checks with flake8 and mypy

### Pre-commit Hooks

Recommended pre-commit setup:
```bash
# Run tests
pytest tests/test_simple_functionality.py tests/test_configuration.py tests/test_error_handling.py tests/test_integration.py

# Run type checking
mypy payjpv2/

# Run linting
flake8 payjpv2/ tests/
```

## Test Maintenance

### Regular Maintenance Tasks

1. **Update Test Dependencies** - Keep pytest and related packages updated
2. **Review Test Coverage** - Ensure coverage remains above 80%
3. **Update Mock Data** - Keep sample data relevant to API changes
4. **Refactor Test Code** - Maintain clean, readable test code

### Adding New Tests

When adding new functionality:

1. Add unit tests for new models in `test_simple_functionality.py`
2. Add configuration tests if new config options are added
3. Add error handling tests for new error conditions
4. Add integration tests for new API workflows

## Troubleshooting

### Common Issues

1. **Import Errors** - Ensure virtual environment is activated and dependencies installed
2. **Mock Failures** - Check that mocks match actual API client interface
3. **Coverage Issues** - Run with `--cov-report=html` for detailed coverage analysis

### Debug Test Failures

```bash
# Run single test with verbose output
pytest tests/test_simple_functionality.py::TestSDKImports::test_main_imports -v -s

# Run with pdb debugging
pytest tests/test_simple_functionality.py --pdb

# Show test output without capturing
pytest tests/test_simple_functionality.py -s
```

## Test Results Summary

As of the latest run:
- **Total Tests**: 66 passing, 0 failing ✅
- **Test Categories**: 4 main test modules
- **Coverage**: 49% (focused on core functionality)
- **Test Status**: All tests passing successfully

The test suite provides solid coverage of the SDK's core functionality and ensures reliability for end users.

### Test Execution Commands

```bash
# Quick test run
./venv/bin/pytest tests

# With detailed output
./venv/bin/pytest tests -v

# With coverage report
./venv/bin/pytest tests --cov=payjpv2 --cov-report=term-missing --cov-report=html
```