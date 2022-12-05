duo_num = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    duo_num = str(n%2) + duo_num
    n //=2
print(duo_num)