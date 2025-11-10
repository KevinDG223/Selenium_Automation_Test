Hi, There 👋

📋 Project Overview

This project is an End-to-End (E2E) automated testing framework built with Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern.
It automates the full purchase flow of an e-commerce demo site, including login, product selection, cart operations, and checkout, using data-driven testing from a JSON file.

A Jenkins pipeline is integrated to execute the tests automatically, demonstrating Continuous Integration (CI) in a professional QA workflow.

🎯 Project Objective

The goal of this project is to:

Demonstrate advanced UI automation using Selenium and Python.

Implement the Page Object Model for maintainable and scalable test code.

Apply data-driven testing for flexible input management.

Showcase integration with Jenkins CI/CD for automated test execution.
🧰 Tech Stack

Language: Python

Framework: Pytest

Automation Tool: Selenium WebDriver

Design Pattern: Page Object Model (POM)

Data Source: JSON file (test_data.json)

Continuous Integration: Jenkins

Test Management: Excel (Test_Cases.xlsx)

Browser: Microsoft Edge

🚀 How It Works

The test script (test_e2e.py) reads user credentials and product data from test_data.json.

Each test case performs the following steps:

1️⃣ Opens the browser and navigates to the e-commerce site.

2️⃣ Logs in using credentials from the JSON file.

3️⃣ Navigates through product categories.

4️⃣ Adds two products (T-shirt and Jeans) to the shopping cart.

5️⃣ Proceeds to checkout and enters payment details.

6️⃣ Validates that the order is successfully confirmed.

Browser type (Edge or Chrome) can be specified via command-line parameters.
(Default: Edge)

[Test_Cases.xlsx](https://github.com/user-attachments/files/23448656/Test_Cases.xlsx)

https://github.com/user-attachments/assets/c71155b2-3680-4d6a-bfde-0b50c6791a77


