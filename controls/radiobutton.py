from selene.support.shared import browser

def gender(gender):
    browser.element(f'[name=gender][value={gender}]+label').click()