# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
# настоящее время.
#
# Одним из атрибутов преступления является его тип – Primary Type.
#
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
#
# Файл с данными:
# https://stepik.org/media/attachments/lesson/24473/Crimes.csv


import csv
import collections


with open("Crimes.csv") as f:
    reader = csv.reader(f)
    counter = collections.Counter()
    for l in reader:
        if '2015' in l[2]:
            counter[l[5]] += 1
    print(counter.most_common(1))

#дату можно было вытащить через datetime.strptime(l[2] r'%m/%d/%Y %H:%M:%S %p')
