# Selenium Automation Script: Search Validation on Selenium Playground

This project contains a Python script that uses **Selenium** and **pytest** to automate the validation of the search functionality on the [Selenium Playground Table Search Demo](https://www.lambdatest.com/selenium-playground/table-sort-search-demo) website. 

## Script Details
- The script navigates to the Selenium Playground Table Search Demo page.
- It interacts with the search box to search for the term **"New York"**.
- It validates the following:
  1. The search results display exactly **5 entries** out of the **24 total entries**.
  2. The total number of entries on the page is **24**.

## Environment Setup
Follow the steps below to set up the environment:

1. **Install Python**: Ensure Python 3.x is installed on your local machine.
   
   You can check your Python version by running:
   ```bash
   python --version

2. **Install Dependencies**: Install dependencies using below command.
    ```bash
    pip install -r requirements.txt

3. **Run Script**: 
    ```bash
    pytest qa_selenium_test.py