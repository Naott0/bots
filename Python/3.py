import time
import turtle

a = int(input("Введите строну №1: "))
b = int(input("Введите строну №2: "))
c = int(input("Введите строну №3: "))
if a + b > c and a + c > b and c + b > a:
    screen = turtle.Screen()
    s = turtle.Turtle()
    for i in range(3):
        s.forward(a)
        s.left(120)
    time.sleep(10)
    print("Треугольник построен ")

else:
    print("Невозможно построить теругольник")

