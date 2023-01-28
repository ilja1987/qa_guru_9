import os.path
from selene.support.shared import browser
from selene import have
from controls import datepicker
from controls import dropdown
from controls import radiobutton
from controls import checkbox

def open_page():
    browser.open('/automation-practice-form')


def fill_user_fields(name, last_name, email, phone, adress):
    browser.element('[id="firstName"]').type(name)
    browser.element('[id="lastName"]').type(last_name)
    browser.element('[id="userEmail"]').type(email)
    browser.element('[id="userNumber"]').type(phone)
    browser.element('#currentAddress').type(adress)


def select_option(selector, text):
    dropdown.select(selector, text)


def select_state(text):
    select_option('#state', text)


def select_sity(text):
    select_option('#city', text)


def select_subjects(text):
    browser.element('[autocapitalize="none"]').type(text).press_tab()


def upload_picture(path_to_photo):
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), path_to_photo)
        )
    )


def select_date_of_birthday(day, month, year):
    datepicker.birthday(day,month,year)


def push_submit_button():
    browser.element('[id="submit"]').press_enter()


def asser_user_registration(name, email, male, phone, birthday, subjects, hobbies, photo, adress, oprions):
    browser.all("tbody tr").should(have.size(10))
    browser.all('tbody tr td:last-child').should(have.texts(
        name, email, male, phone, birthday, subjects, hobbies, photo, adress, oprions))


def select_gender(gender):
    radiobutton.gender(gender)


def select_hobbies(hobies):
    checkbox.hobby(hobies)


