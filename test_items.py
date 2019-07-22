import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_display_for_different_languages(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert button is not None
