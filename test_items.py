import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(3)
    browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')

