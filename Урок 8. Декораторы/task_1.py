import re


def email_parse(email):
    #pattern = re.compile(r"(?P<username>([A-Za-z0-9]+))@(?P<domain>[A-Za-z0-9]+\.[A-Za-z0-9]+)")
    pattern = re.compile(r"(?P<username>.+)@(?P<domain>.+\..+)")
    res = pattern.match(email)
    if not res:
        raise ValueError
    return res.groupdict()


print(email_parse('someone@geekbrains.ru'))
