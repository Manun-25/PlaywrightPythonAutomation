from playwright.sync_api import Page, expect

def test_poi_app_validate(page:Page):
    page.goto("https://poi.apache.org/")
    page.wait_for_timeout(3000)
    expect(page).to_have_url("https://poi.apache.org/")
    expect(page).to_have_title("Apache POI™ - the Java API for Microsoft Documents")