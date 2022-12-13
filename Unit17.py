# словарь per_cent с распределением процентных ставок по вкладам в различных банках
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money - планируемая сумма вклада
money = int(input("Введите сумму вклада: "))
# deposit - список суммы %% за год в каждом банке
deposit = []
deposit.append(int(money * per_cent['ТКБ']/100))
deposit.append(int(money * per_cent['СКБ']/100))
deposit.append(int(money * per_cent['ВТБ']/100))
deposit.append(int(money * per_cent['СБЕР']/100))
print(deposit)
print("Максимальная сумма, которую вы можете заработать —", max(deposit))