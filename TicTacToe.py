field = [[' '] * 3 for i in range(3)]
def welcoming():
    print("""    
Игра крестики-нолики
формат ввода: x, y
x - номер строки
y - номер слобца
отсчёт начинается с нуля
    """)

def p_field():
    for i in field:
        print(*i, sep=' | ')
        print('-' * 9)


def coord():
    while True:

        coords = input("Введите координаты:").split()
        if len(coords) != 2:
            print('Введите 2 координаты')
            continue
        x, y = coords

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите цифры')
            continue

        x, y = int(x), int(y)

        if 0 > x or 0 > y or 2 < x or 2 < y:
            print('Неверные координаты')
            continue

        if field[x][y] != ' ':
            print('Клетка занята')
            continue
        return x, y
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print('Выиграл X!!!')
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

welcoming()
num = 0
while True:
    num += 1
    p_field()
    if num % 2 == 1:
        print('''Ходит "Крестик"''')
    else:
        print(('''Ходит "Нолик"'''))
    x, y = coord()
    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'
    if check_win():
        break
    if num == 9:
        print('Ничья')
        break
