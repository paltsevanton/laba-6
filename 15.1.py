from random import *

unique = []
a = []

while True:
    try:
        M = int(input('Введите M (кол-во строк): '))
        if M < 1:
            print('Ошибка: M должно быть натуральным числом')
            continue
        print("Строк:", M)
        break
    except ValueError:
        print('Ошибка: M должно быть натуральным числом')

while True:
    try:
        N = int(input('Введите N (кол-во столбцов): '))
        if N < 1:
            print('Ошибка: N должно быть натуральным числом')
            continue
        print("Столбцов:", N)
        break
    except ValueError:
        print('Ошибка: N должно быть натуральным числом')

MxN = []

for x in range(M):
    MxN.append([])
    for y in range(N):
        MxN[x].append(randint(-5, 5))

for x in range(len(MxN)):
    for y in range(len(MxN[x])):
        a.append(MxN[x][y])

for i in range(len(a)):
    k = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            k += 1
        if k > 1:
            break
    if k == 1:
        unique.append(a[i])

print('Исходный список: ',MxN)
print('Список неповторяющихся элементов: ',unique)