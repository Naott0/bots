a = int(input('Введите число N: '))
o = 1
for i in range(a):
    b = int(input(f'Введите число №{o}: '))
    o += 1
    if b % 3 == 0 and b % 5 == 0:
        print('FizzBuzz')

    elif b % 5 == 0:
        print('Buzz')

    else:
        b % 3 == 0
        print('Fizz')