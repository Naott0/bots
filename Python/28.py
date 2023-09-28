
# 28
# разработать декоратор, который добавит к строке, возвращаемой функцией заданный копирайт
def copyrite(f):
    def inner(*args, **kwargs):
        return f(*args, **kwargs) + '\n(c) Иванов И.И.'

    return inner

@copyrite
def citata():
    x = str(input('Ввидте цитату: '))
    return x

print(citata())