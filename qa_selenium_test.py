import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture to set up WebDriver
@pytest.fixture
def setup():
    # Setup Chrome WebDriver with options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    
    # Initialize WebDriver and install the appropriate ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Yield the driver so it can be used in tests
    yield driver
    
    # Teardown: Close the WebDriver after the test is complete
    driver.quit()


# Test to search funcationality on the Selenium Playground
def test_search_functionality(setup):

    # Go to the Selenium Playground page
    setup.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    
    # Locate the search input field
    search_box = setup.find_element(By.XPATH, '//*[@id="example_filter"]/label/input')
    print(f"Searching for New York city")
    search_box.clear()
    search_box.send_keys("New York")
    
    # Wait for results to load and assert that there are 5 results
    WebDriverWait(setup, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="example"]/tbody/tr'))
    )
    rows = setup.find_elements(By.XPATH, '//*[@id="example"]/tbody/tr')
    print(f"total rows returned :: {len(rows)}")
    assert len(rows) == 5, f"Expected 5 rows, but found {len(rows)}"

# Test to validate that the total entries on the page are 24
def test_total_entries(setup):
    # Navigate to the page
    setup.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    
    # Check for the total entries displayed
    total_entries_text = WebDriverWait(setup, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="example_info"]'))
    ).text
    print(f"total_entries_text :: {total_entries_text}")
    assert "Showing 1 to 10 of 24 entries" in total_entries_text, f"Expected total entries to be 24, but got: {total_entries_text}"
