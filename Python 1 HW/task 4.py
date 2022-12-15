# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

while True:
    try:
        numberOfQuarter = int(input("Введите номер четверти: "))
    except ValueError:
        print("Вы вводите не цифровые значения, попробуйте еще раз")
        continue
    break

if numberOfQuarter == 1:
    print("Координата x > 0, координата y > 0")
elif numberOfQuarter == 2:
    print("Координата x < 0, координата y > 0")
elif numberOfQuarter == 3:
    print("Координата x < 0, координата y < 0")
elif numberOfQuarter == 4:
    print("Координата x > 0, координата y < 0")
else:
    print("Вы ввели некорректный набор цифровых данных")