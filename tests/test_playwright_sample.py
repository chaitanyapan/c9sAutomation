from playwright.sync_api import sync_playwright

def test_example_dot_com_title():
    with sync_playwright() as p:
        # Launch browser (headless by default)
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to website
        page.goto("https://example.com")

        # Assertion
        assert "Example Domain" in page.title()

        # Close browser
        browser.close()
