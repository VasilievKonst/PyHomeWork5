import random

print("Добро пожаловать в игру!")
pl_1 = input('Игрок, введите ваше имя: ')
pl_2 = "BOT"

print(f'{pl_1}, вы играете против бота. Добро пожаловать в игру!')

all_konf = 2021
all_konf_1 = 0
all_konf_2 = 0

def takek(pl_n):
    x = int(input(f'{pl_n}, укажите сколько конфет вы возьмете: '))
    if (x < 0) or (x > 28):
        print('Бери меньше! Не больше 28!')
        return takek(pl_n)
    else:
        return x 

def step_info(c, a, b, v):
    print(f"{c}, вы взяли {a} и у вас {b} конфет. В игре остается {v} конфет.")

def intel(value):
    k = random.randint(1, 29)
    while value-k <= 28 and value > 29:
        k = randint(1, 29)
    return k

flag = random.randint(0, 1)
if flag:
    print(f"Первый ходит {pl_1}")
else:
    print(f"Первый ходит {pl_2}")

while all_konf > 28:
    if flag:
        k = takek(pl_1)
        all_konf_1 += k
        all_konf -= k
        flag = False
        step_info(pl_1, k, all_konf_1, all_konf)
    else:
        k = intel(all_konf)
        all_konf_2 += k
        all_konf -= k
        flag = True
        step_info(pl_2, k, all_konf_2, all_konf)

if flag:
    print(f"Выиграл {pl_1} и ему достаются все конфеты!")
else:
    print(f"Выиграл {pl_2} и ему достаются все конфеты!")
