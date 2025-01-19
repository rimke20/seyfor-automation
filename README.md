# Automation Testing

This repository contains UI automation tests for issuing invoices. The test file is seperate from variable and utils file to keep code more clean and readable. Utils file is inteded to keep shared logic and reusable code.

## Pre-requirements

Before running the tests, make sure to have the appropriate drivers installed:

- **Python**: Python needs to be installed on your machine. If it is not already installed, download and install the latest version
- **For Chrome**: Download and install [ChromeDriver].

## Test Notes
- I have included the flow that was described in the assignment sent in the email. The test coveres basic assertions to verify that the invoices have the correct amounts and items displayed.
- If I were to continue developing the tests I would add deletion of customers and articles in my teardown method.
- Test were run only on Chrome browser, if the case was to cover everything additional browsers would have been added.

## How to Run

1. Run pip install -r requirements.txt
3. To run the tests: python automation-tests/invoice_issued.py 




