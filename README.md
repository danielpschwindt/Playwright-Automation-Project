Playwright UI Automation Framework (Python)
Overview

This project is a UI test automation framework built using Playwright and Pytest.

It demonstrates a structured and scalable automation architecture including:

Page Object Model (POM)

Config-driven test execution

Parallel test execution

HTML reporting

Logging system

Automatic screenshot capture on failure

Git version control

The goal of this project is to showcase real-world automation framework design principles.

Tech Stack

Python

Playwright

Pytest

Git

pytest-html (HTML reporting)

Python logging module

pytest-xdist (parallel execution)

Project Structure
qa_project_1/
│
├── tests/                  # Test cases
├── pages/                  # Page Object Models
├── utils/                  # Utilities (logger, config reader)
├── config/                 # Environment configuration
├── screenshots/            # Failure screenshots
├── conftest.py             # Pytest fixtures and hooks
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
├── automation.log          # Generated log file
└── README.md
Features
Page Object Model (POM)

Separates test logic from UI interaction logic for maintainability and scalability.

Config-Driven Execution

Environment values are stored in a configuration file to avoid hardcoding.

Parallel Test Execution

Tests can run in parallel using pytest-xdist.

HTML Reporting

Automatic generation of an HTML test report.

Logging System

Test execution details are saved in automation.log.

Screenshot on Failure

When a test fails, a screenshot is automatically saved in the screenshots/ folder.

Git Version Control

The project is tracked using Git with structured commits.

Installation and Setup
1. Clone the Repository
git clone <your-repo-url>
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

Run tests in parallel:

pytest -n 4

Generate HTML report:

pytest --html=report.html
Screenshot Feature

If a test fails, a screenshot is automatically saved inside the screenshots directory.
The filename includes the test name and timestamp.

Logging

Execution logs are saved in:

automation.log

This file records important runtime information for debugging.

Future Improvements

Continuous Integration with GitHub Actions

Docker containerization

API automation framework

Cross-browser test matrix

Advanced reporting (Allure)

Smoke and regression test tagging

Purpose

This project demonstrates:

Automation framework design

Clean architecture principles

Scalable test structure

Professional QA engineering practices

If you’d like, I can now help you:

Make this README more advanced

Add badges

Add a CI pipeline

Or begin Project 2 (API automation)
