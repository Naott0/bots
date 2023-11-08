import folium

location1 = (input('введите широту: '))
location2 = (input('введите долготу: '))
# 47.2610085, 39.6279999
print(location1)
palce = folium.Map(location=[location1, location2])

palce.save('index.html')
print('Finish')
