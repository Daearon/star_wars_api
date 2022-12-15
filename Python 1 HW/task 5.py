# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math

while True:
    try:
        xa = float(input("Введите координату xa: "))
    except ValueError:
        print("Вы вводите не цифровые значения, попробуйте еще раз")
        continue
    break
while True:
    try:
        xb = float(input("Введите координату xb: "))
    except ValueError:
        print("Вы вводите не цифровые значения, попробуйте еще раз")
        continue
    break
while True:
    try:
        ya = float(input("Введите координату ya: "))
    except ValueError:
        print("Вы вводите не цифровые значения, попробуйте еще раз")
        continue
    break
while True:
    try:
        yb = float(input("Введите координату yb: "))
    except ValueError:
        print("Вы вводите не цифровые значения, попробуйте еще раз")
        continue
    break


def FindDistance (firstX, secondX, firstY, secondY):
    return math.sqrt((secondX - firstX) ** 2 + (secondY - firstY) ** 2)

distance = FindDistance(xa, xb, ya, yb)
print(distance)