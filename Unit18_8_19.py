tickets_count = int(input("Введите количество билетов:"))
sum = 0
for ticket in range (1, tickets_count + 1):
    age = int(input(f"Введите возраст посетителя по билету {ticket}:"))
    if 18 <= age < 25:
        sum += 990
    elif age >= 25:
        sum += 1390
if tickets_count > 3:
    sum = sum - sum*0.1
print(f"Сумма к оплате: {sum} руб.")