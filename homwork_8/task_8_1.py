import re
EMAIL = re.compile(r'(^[a-z0-9]+)@([a-z0-9]+\.[a-z]+$)')

def email_parse(email):
    information = EMAIL.findall(email)
    if information:
        name, mail_domain = information[0]
    else:
        raise ValueError(f'wrong email {email}')
    print(name, mail_domain)

email_parse('someone@geekbrains.ru')
email_parse('someone@123@geekbrains.ru')
