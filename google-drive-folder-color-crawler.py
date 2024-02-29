from playwright import sync_playwright
from bs4 import BeautifulSoup
import re

# Launch the Firefox browser
with sync_playwright() as playwright:
    browser = playwright.firefox.launch()

    # Create a new browser context
    context = browser.new_context()

    # Create a new page
    page = context.new_page()

    # Navigate to the specific page
    page.goto('https://example.com')

    html_content = page.content()

    # Find an element with a specific 'aria' attribute
    element = page.query_selector('[aria-label="example"]')

    # Do something with the element
    if element:
        # Perform actions on the element
        # For example, get the text content of the element
        text_content = element.text_content()
        print(text_content)

    # Close the browser
    context.close()
    browser.close()

# Assuming 'html' is your HTML document
soup = BeautifulSoup(html_content, 'html.parser')

# Find elements where attribute name contains 'aria'
elements = soup.find_all(lambda tag: any(re.match(r'.*aria.*', attr) for attr in tag.attrs))

# Now 'elements' contains all elements with an attribute containing 'aria'