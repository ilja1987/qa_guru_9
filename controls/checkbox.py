from selene.support.shared import browser
from selene import have
def hobby(hobies):
    checkboxes_click(browser.all('[for^=hobbies-checkbox]'), hobies)


def checkboxes_click(elements, *by_texts):
    for value in by_texts:
        elements.element_by(have.text(value)).click()