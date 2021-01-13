# Вам дана в архиве (https://stepik.org/media/attachments/lesson/24465/main.zip) файловая структура,
# состоящая из директорий и файлов.
#
# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых
# есть хотя бы один файл с расширением ".py".
#
# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в
# лексикографическом порядке.
#
# Для лучшего понимания формата задачи, ознакомьтесь с примером.
# Пример архива: https://stepik.org/media/attachments/lesson/24465/sample.zip
# Пример ответа: https://stepik.org/media/attachments/lesson/24465/sample_ans.txt

import os
import os.path

lst = []
for root, dirs, files in os.walk('./main'):
    for f in files:
        if f[-3:] == '.py':
            lst.append(root[2:])
            break

with open('out.txt', 'w') as f_out:
    txt = '\n'.join(sorted(lst))
    f_out.write(txt)