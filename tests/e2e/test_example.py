import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("Första")
    first_button.click(timeout=100)

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(sp_button).to_be_visible()