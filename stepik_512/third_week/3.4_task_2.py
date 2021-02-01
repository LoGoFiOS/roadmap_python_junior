# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть
# поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
#
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
#
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется
# явно от одного класса более одного раза.
#
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
# <имя класса> : <количество потомков>
#
# Выводить классы следует в лексикографическом порядке.

import json
import collections


def get_index(v):
    """Get index in json data for vertex v"""
    for i in data_json:
        if i['name'] == v:
            return i


def dfs(v, visited):
    visited.add(v)

    for p in get_index(v)['parents']:
        if p not in visited:
            answer[p] += 1
            dfs(p, visited)


data_json = json.loads(input())

answer = collections.Counter()
for i in data_json:
    answer[i['name']] += 1
    visited = set()
    dfs(i['name'], visited)

for i in sorted(answer.items(), key=lambda x: x[0]):
    print(f'{i[0]} : {i[1]}')
