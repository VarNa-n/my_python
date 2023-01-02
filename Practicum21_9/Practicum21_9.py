class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'

    def get_area(self):
        return self.width * self.height


# 21.9.1
rect_1=Rectangle(5,10,50,100)
print(rect_1)

# 21.9.2
print("Area: ", rect_1.get_area())

class Client:
    def __init__(self, name, surname, city, account = 0):
        self.name = name
        self.surname = surname
        self.city = city
        self.account = account

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.account} руб.'

    def guest_list(self):
        return f'{self.name} {self.surname}, {self.city}'

client = []
# 21.9.3
client.append(Client('Иван', 'Петров', 'Москва', 50))
print(client[0])

# 21.9.4
client.append(Client('Петр', 'Иванов', 'СПб'))
client.append(Client('Андрей', 'Кузнецов', 'Воронеж'))
client.append(Client('Олег', 'Куликов', 'Москва'))

print("Guest list:")
for cli in sorted(client, key=lambda x: x.name):
    print(cli.guest_list())


