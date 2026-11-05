from playwright.sync_api import Page, expect

def test_launch_poiapache(page:Page):
    page.goto("https://poi.apache.org/")
    page.wait_for_timeout(3000)
    url=page.url
    print("URL of Application: ", url)
    title=page.title()
    print("Title of Application: ", title)