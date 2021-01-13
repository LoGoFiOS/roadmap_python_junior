# Алиса владеет интересной информацией, которую хочет заполучить Боб.
# Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
# У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.
#
# Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог
# понять какой из паролей ему нужен. Помогите ему решить эту проблему.
#
# Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
# Она представила информацию в виде строки, и затем записала в бинарный файл результат работы
# метода simplecrypt.encrypt.
#
# Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать,
# какой из паролей служит ключом для расшифровки файла с интересной информацией.
#
# Ответом для данной задачи служит расшифрованная интересная информация Алисы.
#
# Файл с информацией: https://stepik.org/media/attachments/lesson/24466/encrypted.bin
# Файл с паролями:https://stepik.org/media/attachments/lesson/24466/passwords.txt


from simplecrypt import decrypt

with open('encrypted.bin', 'rb') as encrypted:
    msg = encrypted.read()

with open('passwords.txt', 'rt') as passwords:
    lines = (line.strip() for line in passwords)
    for line in lines:
        print(line)
        try:
            print(decrypt(line, msg))
        except:
            print('Error')