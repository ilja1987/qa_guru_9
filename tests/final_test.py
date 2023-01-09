import pages.practice_form as p


def test_form(browser_setup):
    p.open_page()
    p.fill_user_fields('Ilja',
                     'Domnin',
                     'domniniv@mail.ru',
                     '89051010101',
                     'Sad area, Dreary area, Sadness, Disappointment Avenue, house 13')

    p.select_date_of_birthday(5, 2, 1987)

    p.select_subjects('maths')
    p.select_subjects('chemistry')

    p.select_gender('Male')

    p.select_hobbies('Reading')

    p.upload_picture('../resources/foto.bmp')

    p.select_state('NCR')
    p.select_sity('Delhi')

    p.push_submit_button()

    p.asser_user_registration('Ilja Domnin',
                            'domniniv@mail.ru',
                            'Male',
                            '8905101010',
                            '05 February,1987',
                            'Maths, Chemistry',
                            'Reading',
                            'foto.bmp',
                            'Sad area, Dreary area, Sadness, Disappointment Avenue, house 13',
                            'NCR Delhi')



