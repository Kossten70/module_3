def send_email(message, recipient, sender = "university.help@gmail.com"):
    if '@' not in recipient or not recipient.endswish('.com', 'ru', 'net') and'@' not in sender or not sender.endswish('.com', 'ru', 'net'):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса: ', sender)




send_email('Это сообщение для проверки связи', 'm1525@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
