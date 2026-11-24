while True:
    try:
        n = int(input("Введите кол-во стран: "))
        if n < 1:
            print('Ошибка: n должно быть натуральным числом')
            continue
        print("Кол-во стран:", n)
        break
    except ValueError:
        print('Ошибка: n должно быть натуральным числом')

d = {}

for i in range(n):
    k = input('Введите страну и список рек в ней через пробел: ').split()
    d[k[0]] = [k[x] for x in range(1, len(k))]

while True:
    q = input('Введите названия рек через пробел: ').split()
    if not q:
        print('Ошибка: не введено ни одной реки')
        continue
    break

for target_river in q:
    found_countries = []
    for country, rivers in d.items():
        if target_river in rivers:
            found_countries.append(country)

    if found_countries:
        print('Река', target_river, 'найдена в странах:', ', '.join(found_countries))
    else:
        print("Страна с рекой", target_river, "не найдена")