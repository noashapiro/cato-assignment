# Cato assignment Test Automation

Automated testing for DemoBlaze site using Playwright and pytest.

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

### Local

```bash
# Generate report
pytest --alluredir=reports/allure

# View report
allure serve reports/allure
```

### Docker

```bash
# Run tests and extract reports
docker run --rm -v $(pwd)/reports:/app/reports cato-tests

# View extracted report
allure serve reports/allure
```

## Configuration

- `configuration.py` - Base URL, timeout, headless mode
- `logger_config.py` - Logging setup
- `pytest.ini` - Parallel execution (8 workers by default)
