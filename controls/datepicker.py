from selene.support.shared import browser


def birthday(day, month, year):
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element(f'[value="{month - 1}"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(f'[value = "{year}"]').click()
    browser.element(f'.react-datepicker__day--00{day}').click()
