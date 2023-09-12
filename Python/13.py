# 13
# Задача от СБЕРа
# ввести число n
# Построить из единиц пирамиду высотой n

edinica = '1'
probel = '_'
x = int(input('введите число: '))
count = 1
for i in range(x):
    print(probel * (x - 1 - i), edinica * count, sep='')
    count += 2
