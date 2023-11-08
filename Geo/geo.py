import folium

x = int(input('введите широту: '))
y = int(input('ведите долготу: '))


def geo(x, y):
    print(x, y)
    palce = folium.Map(location=[x, y])
    palce.save('index.html')
    print('Finish')


# 47.2610085, 39.6279999
geo(x, y)
