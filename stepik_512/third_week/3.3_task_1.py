# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно
# с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход
# и из C в B можно перейти за один переход.
#
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
#
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.
#
# Sample Input 1:
# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample2.html
#
# Sample Output 1:
# Yes


import re
import requests


def is_url_valid(url):
    html = requests.get(url)
    return html.status_code == 200


def get_urls(html):
    template = r"\"(?P<url>.+?)\""
    return [i for i in re.findall(template, html) if is_url_valid(i)]


a, b = (input() for _ in range(2))
answer = 'No'
if is_url_valid(a):
    html_a = requests.get(a)
    for i in get_urls(html_a.text):
        html_c = requests.get(i)
        if b in get_urls(html_c.text):
            answer = 'Yes'
            break
print(answer)