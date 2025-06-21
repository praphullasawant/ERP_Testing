from playwright.sync_api import expect

def test_login_redirects_to_profile(login):
    expect(login).to_have_url("http://localhost:3000/profile")
