n = int(input("Введите число: "))

def fibonacci(n):
    a, b = 1, -1
    for i in range(n):
        yield a
        a, b = b, a - b

data1 = list(fibonacci(n))
data1_rev = list(reversed(data1))

z = n
def fibonacci(z):
    a, b = 0, 1
    for i in range(z):
        yield a
        a, b = b, a + b
data = list(fibonacci(z))

print(data1_rev + data)