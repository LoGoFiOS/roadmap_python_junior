# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
#
# Пример входного файла:
# ab
# c
# dde
# ff
#
# Пример выходного файла:
# ff
# dde
# c
# ab


lines = []
with open("text_in.txt") as f_in, open("text_out.txt", "w") as f_out:
    for line in f_in:
        lines.append(line.rstrip())

    for i in reversed(lines):
        f_out.write(i + "\n")