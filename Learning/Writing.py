# cities = ['Adelaide', 'Alice Springs', "Darwin", "Melbourne", "Sydney"]
# with open("D:\Python file\cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

cities = []
with open('D:\Python file\cities.txt', 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))
print(cities)
for city in cities:
    print(city)
