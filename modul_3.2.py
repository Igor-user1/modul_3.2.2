at_ = '@'
end_1 = '.com'
end_2 = '.ru'
end_3 = '.net'


def send_email(message, recipient, sender='university.help@gmail.net'):
    global at_, end_1, end_2, end_3

    if at_ not in recipient:
        print('Невозможно отправить письмо с адреса ' + sender + ' на адрес ' + recipient)
        return

    if at_ not in sender:
        print('Невозможно отправить письмо с адреса ' + sender + ' на адрес ' + recipient)
        return

    if end_1 in recipient:
        print('')
    elif end_2 in recipient:
        print('')
    elif end_3 in recipient:
        print('')
    else:
        print('Невозможно отправить письмо с адреса ' + sender + ' на адрес ' + recipient)
        return

    if end_1 in sender:
        print('')
    elif end_2 in sender:
        print('')
    elif end_3 in sender:
        print('')
    else:
        print('Невозможно отправить письмо с адреса ' + sender + ' на адрес ' + recipient)
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса ' + sender + ' на адрес '+recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ' + sender + ' на адрес ' + recipient)
        return
    return


send_email('Привет!', 'university.help@gmail.net')
