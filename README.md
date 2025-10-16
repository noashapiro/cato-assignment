# DemoBlaze Test Automation

Automated testing for DemoBlaze e-commerce site using Playwright and pytest.

## Quick Start

### Local Setup

```bash
# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Run tests
pytest -v

# Run with visible browser (for debugging)
pytest -v -n 0

# Run with custom parallel workers
pytest -v -n 4
```

### Docker

```bash
# Build and run
./docker-run.sh

# Or manually
docker build -t cato-tests .
docker run --rm cato-tests
```

## Allure Reports

```bash
# Generate report
pytest --alluredir=reports/allure

# View report
allure serve reports/allure
```

## Project Structure

```
ui/
├── locators/          # Element selectors
├── pages/             # Page objects
└── tests/             # Test cases
```

## Configuration

- `configuration.py` - Base URL, timeout, headless mode
- `logger_config.py` - Logging setup
- `pytest.ini` - Parallel execution (8 workers by default)
