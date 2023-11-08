import folium

# location1 = (input('введите координаты широту и долготу: '))
# 47.2610085, 39.6279999
palce = folium.Map(location=[47.2610085, 39.6279999])
palce.save('index.html')
