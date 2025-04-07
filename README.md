# CI/CD Hello World with Python & GitHub Actions

This is a simple CI/CD pipeline built using GitHub Actions to automate testing and deployment for a Python application.

## Project Overview

This project demonstrates the basics of Continuous Integration (CI) and Continuous Deployment (CD) using GitHub Actions. It contains:
- A simple Python application that greets the user.
- Automated tests to ensure the application is functioning as expected.
- A CI/CD pipeline using GitHub Actions to:
  1. Run the tests automatically when changes are pushed.
  2. Simulate deployment after successful tests.

## How It Works

1. **Python Application**: The app prints a greeting message.
2. **Automated Tests**: The test file verifies that the greeting function works correctly.
3. **CI/CD Pipeline**: The GitHub Actions workflow is triggered on each push to the `main` branch. It performs the following steps:
   - Checks out the code
   - Installs dependencies
   - Runs tests
   - If tests pass, it simulates a deployment (just prints a message for now).

## Tech Stack

- Python 3.10
- GitHub Actions for CI/CD
- pytest for testing

## Setup and Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ci-cd-hello-world.git
   cd ci-cd-hello-world
