# TestCars Project

## Flask Cars API with UI and Tests

This is a simple Flask application where you can add and delete cars via API and view them through a web interface. The project includes both API tests and UI tests using Playwright.

## Features
- **Flask API**: Allows adding and deleting cars.
- **Web Interface**: Displays a list of cars and provides a form to add a new car.
- **Tests**:
  - **API Tests**: Tests for adding, retrieving, and deleting cars via the API.
  - **UI Tests**: Tests for interacting with the web interface, ensuring that the car list is properly displayed and cars can be added through the UI.

## Requirements

To get started with the project, you'll need Python 3.7 or later. The required dependencies can be installed via `pip`.

### 1. Install dependencies

Create a virtual environment and install the required dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate



###!!!Test execution order!!!###
1.Launch flask app / python app.py
2.Launch API tests / pytest -s -v tests/test_app_api.py
3.Launch UI tests / pytest -s -v test/test_cars.py
