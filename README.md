Hi, There 👋

📋 Project Overview

The goal of this project is to automate a full purchase flow in an online store using test data from a JSON file.
The automated test performs the following actions:

*Opens the e-commerce website.

*Logs in using valid credentials.

*Navigates through product categories.

*Adds two products (T-shirt and Jeans) to the cart.

*Proceeds to checkout and enters payment details.

*Validates that the order is successfully placed.

🎯 Project Objective

*The goal of this project is to demonstrate a scalable and maintainable automation framework capable of handling:

*Dynamic test data

*Multiple browsers

*Modular and reusable page objects

*Clear and readable test flows

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

⚙️ Tech Stack

*Python

*Selenium WebDriver

*Pytest

*Page Object Model (POM)

*JSON Data-Driven Testing
