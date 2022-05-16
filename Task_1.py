import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if RE_MAIL.match(email) != None:
        for i in range(len(email)):
            if email[i] == '@':
                string_for_username = email[:i]
                string_for_domain = email[i+1:]
        dickt = {'username': string_for_username, 'domain': string_for_domain}
        return dickt
    else:
        raise ValueError(f'wrong email: {email}')


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('nothing@shmail.cm'))
    print(email_parse('someone@geekbrainsru'))

