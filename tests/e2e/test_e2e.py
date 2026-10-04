import re
from playwright.sync_api import Page, expect

# Testar user story 2 - Daily standup
def test_daily_standup(page: Page):

    # Gå till sidan
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("Första")
    first_button.click(timeout=100)

    # Hitta button med texten "Daily standup"
    ds_button = page.get_by_role("button").get_by_text(re.compile("Daily standup"))
    expect(ds_button).to_be_visible()


# Testar User story 3 - Timmer i Daily standup
def test_start_daily_standup_timer(page: Page):

    # Gå till sidan
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Välj första dagen i sprinten
    page.get_by_role("button", name="Första").click()

    # Öppna Daily standup
    page.get_by_role("button", name="Börja varje dag med Daily standup").click()

    # Startar timern
    page.get_by_role("button",name="Börja mötet: 10 minuter").click()

    # Kontrollera att timern innehåller inte --:--
    timer_text = page.get_by_text("--:--")
    expect(timer_text).not_to_be_visible()


# Testar user story 5 - Språkval
def test_change_language(page: Page):

    # Gå till agile-helper
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Kontrollera svensk text
    day_text = page.get_by_text("Vilken dag under sprinten är det?")
    expect(day_text).to_be_visible()

    # Klicka på engelska flaggan
    page.get_by_test_id("language-en").click()

    # Kontrollera engelsk text
    day_text = page.get_by_text("What day of the sprint is it?")
    expect(day_text).to_be_visible()

    # Kontrollera knapparna är på engelska
    expect(page.get_by_role("button", name="First")).to_be_visible()
    expect(page.get_by_role("button", name="Somewhere in the middle")).to_be_visible()
    expect(page.get_by_role("button", name="Last")).to_be_visible()

    # Klicka på svenska flaggan
    page.get_by_test_id("language-sv").click()

    # Kontrollera svensk text igen
    day_text = page.get_by_text("Vilken dag under sprinten är det?")
    expect(day_text).to_be_visible()

    # Kontrollera knapparna är på engelska
    expect(page.get_by_role("button", name="Första")).to_be_visible()
    expect(page.get_by_role("button", name="Någonstans mitt i")).to_be_visible()
    expect(page.get_by_role("button", name="Sista")).to_be_visible()

