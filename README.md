Playwright UI Automation Framework

A scalable UI test automation framework built with Playwright and Pytest, designed using modern automation architecture principles.

Overview

This project demonstrates a production-style UI automation framework featuring:

Page Object Model (POM)

Config-driven execution

Parallel test execution

HTML reporting

Logging system

Automatic screenshot capture on failure

Git version control

The framework is structured for maintainability, scalability, and real-world automation practices.

Tech Stack

Python

Playwright

Pytest

pytest-html

pytest-xdist

Git

Project Structure
qa_project_1/
│
├── tests/              # Test cases
├── pages/              # Page Object Models
├── utils/              # Utilities (logger, config)
├── config/             # Environment configuration
├── screenshots/        # Failure screenshots
├── conftest.py         # Pytest fixtures & hooks
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Dependencies
├── automation.log      # Generated log file
└── README.md
Features
Page Object Model

Separates test logic from UI interaction logic to improve maintainability.

Config-Driven Execution

Environment values are stored externally to avoid hardcoding.

Parallel Execution

Supports parallel test runs using pytest-xdist.

HTML Reporting

Automatically generates an HTML test report.

Logging

Execution details are recorded in automation.log.

Screenshot on Failure

Automatically captures screenshots when tests fail.

Installation
1. Clone the Repository
git clone <repository-url>
cd qa_project_1
2. Create Virtual Environment
python -m venv venv

Activate (Windows):

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
playwright install
Running Tests

Run all tests:

pytest

Run in parallel:

pytest -n 4

Generate HTML report:

pytest --html=report.html
Reporting

After execution:

HTML report is generated in the project root.

Logs are stored in automation.log.

Failure screenshots are saved in the screenshots/ directory.

Future Enhancements

Continuous Integration with GitHub Actions

Docker containerization

API automation framework

Cross-browser test matrix

Advanced reporting integration

Smoke and regression test tagging

Purpose of This Project

This framework was built to demonstrate:

Automation architecture design

Clean code organization

Scalable test structure

Real-world QA engineering practices
