per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада:'))
for values in per_cent:
    per_cent[values] = per_cent[values]*money/100
deposit = list(per_cent.values())
deposit[1] = int(max(deposit))
print('Максимальная сумма, которую вы можете заработать —', deposit[1])




