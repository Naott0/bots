# можно сделать срезом но сделал так
a = input('Введите числа: ')
count = (-abs(int(input('Введите число для сдвига: ')))+1)
count2 = abs(count)
g=[]
for i in a:
    g += (a[count]).split()
    count += 1
print(g)