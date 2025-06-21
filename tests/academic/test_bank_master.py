def test_add_bank_details(login):
    page = login

    page.get_by_role("link", name="Academic").click()
    page.get_by_role("link", name="Master").click()
    page.get_by_role("link", name="Academic Master").click()
    page.get_by_role("link", name="Bank Details").click()

    page.get_by_role("textbox", name="Please Enter Bank Code").fill("B1")
    page.get_by_role("textbox", name="Please Enter Bank Name").fill("Bank")
    page.get_by_role("textbox", name="Please Enter Bank Address").fill("Pune, Maharashtra")
    page.get_by_role("button", name="Submit").click()

    page.get_by_role("tab", name="Bank Account").click()
    page.locator("#bank").select_option("102")
    page.get_by_role("textbox", name="Please Enter Account No.").fill("123456789")
    page.get_by_role("button", name="Submit").click()
