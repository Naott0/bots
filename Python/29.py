
text = list(input('Введите текст: '))
for i in text[::-1]:
    if i in 'а, я, у, ю, о, е, ё, э, и, ы':
        text.remove(i)
print(text)
