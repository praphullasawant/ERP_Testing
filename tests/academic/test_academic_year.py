from playwright.sync_api import expect

def test_add_academic_year(login):
    page = login

    page.get_by_role("link", name="Academic").click()
    page.get_by_role("link", name="Master").click()
    page.get_by_role("link", name="Academic Master").click()
    page.get_by_role("link", name="Academic Year").click()

    page.get_by_role("textbox", name="Please Enter Academic Year/").fill("2025-26")
    page.get_by_placeholder("Please Enter Start Date").fill("2025-06-01")
    page.get_by_role("textbox", name="Please Enter Short Name").fill("25_26")
    page.get_by_placeholder("Please Enter End Date").fill("2025-06-30")
    page.get_by_role("checkbox", name="Check If Active").uncheck()
    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_text("Data Submitted Successfully!!!")).to_be_visible()


def test_add_concession(login):
    page = login

    page.get_by_role("link", name="Academic").click()
    page.get_by_role("link", name="Master").click()
    page.get_by_role("link", name="Academic Master").click()
    page.get_by_role("link", name="Concession").click()
    page.get_by_role("textbox", name="Please Enter Short Name").click()
    page.get_by_role("textbox", name="Please Enter Short Name").fill("Con1")
    page.get_by_role("textbox", name="Please Enter Concession").click()
    page.get_by_role("textbox", name="Please Enter Concession").fill("ConcessionOne")
    page.get_by_role("textbox", name="Please Enter Percentage").click()
    page.get_by_role("textbox", name="Please Enter Percentage").fill("20")
    page.get_by_role("button", name="Submit").click()

