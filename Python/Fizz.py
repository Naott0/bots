x = int(input('Введите число N: '))

for i in range(1, x+1):
    if i % 3 == 0 and i % 5 == 0:
        print(f'Число {i}''-''FizzBuzz')

    elif i % 5 == 0:
        print(f'Число {i}''-''Buzz')

    else:
        i % 3 == 0
        print(f'Число {i}''-''Fizz')