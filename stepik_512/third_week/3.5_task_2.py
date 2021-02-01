# В этой задаче вам необходимо воспользоваться API сайта artsy.net
#
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
#
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
#
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
# выведите их имена в лексикографическом порядке.


import requests
import json
import sys

client_id = ''
client_secret = ''

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
# разбираем ответ сервера
j = json.loads(r.text)
# получаем токен
token = j["token"]


def req(id, answer):
    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token": token}
    # инициируем запрос с заголовком
    r = requests.get(f"https://api.artsy.net/api/artists/{id.strip()}", headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)
    answer[j['sortable_name']] = j['birthday']


answer = {}
for id in sys.stdin:
    req(id, answer)

for i in sorted(answer.items(), key=lambda x: (x[1], x[0])):
    print(i[0])