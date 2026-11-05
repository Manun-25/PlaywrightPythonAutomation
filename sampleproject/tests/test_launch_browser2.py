from playwright.sync_api import sync_playwright, Page, expect

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://poi.apache.org/")
    page.wait_for_timeout(3000)
    url=page.url
    print("URL of Application: ", url)
    title=page.title()
    print("Title of Application: ", title)