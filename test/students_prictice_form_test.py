from demo_qa.model.pages import students_form


def test_filled_form():
    students_form.open_page()

    # WHEN
    students_form.input_info(name='Dmitry',
                             surname='Yanyshev',
                             email='dima-xxx@mail.ru',
                             mobile='1234567890',
                             address='Kazan'
                             )

    students_form.select_gender('Male')

    students_form.select_birthday(day='06', month='3', year='1995')

    students_form.input_subject('Computer Science')

    students_form.select_hobbies('Music', 'Sports')

    students_form.upload_picture('resource/image.jpg')

    students_form.select_state('NCR')
    students_form.select_city('Delhi')

    students_form.submit()

    # THEN

    students_form.assert_of_registered_user(
            'Dmitry Yanyshev',
            'dima-xxx@mail.ru',
            'Male',
            '1234567890',
            '06 April,1995',
            'Computer Science',
            'Music, Sports',
            'image.jpg',
            'Kazan',
            'NCR Delhi'
    )
