# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - TBD

### Added
- Initial release of PAY.JP Python SDK v2
- Complete Python client library for PAY.JP v2 API
- Support for all PAY.JP v2 API endpoints:
  - Customers API
  - Payment Intents API  
  - Payment Methods API
  - Setup Intents API
  - Products API
  - Prices API
  - Plans API
  - Tax Rates API
  - Checkout Sessions API
  - Payment Pages API
  - Refunds API
  - Elements API
- Full type annotations with Pydantic v2 models
- Comprehensive test coverage
- Auto-generated API documentation

### Changed
- Unified package name to `payjpv2`
- Updated package metadata with proper PAY.JP branding
- Standardized Python version requirement to 3.8+
- Improved security in example code with environment variable usage
- Enhanced .gitignore to exclude development files

### Security
- Removed hardcoded API keys from example code
- Added environment variable-based configuration
- Updated default host to production PAY.JP API endpoint

### Infrastructure
- Added MIT License
- Implemented automated release workflow for PyPI
- Enhanced CI/CD with proper Python testing matrix
- Added comprehensive .gitignore for Python development