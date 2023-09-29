import numpy as np

f = open(r'C:\Users\shashg\Downloads\test_data.txt')
total_lines = f.readlines()
matrix =[]
for line in total_lines:
    num = []
    items = line.split(" ")
    for item in items:
        try:
            num.append(int(item))
        except:
            continue
    if len(num) > 0:
        matrix.append(num)
matrix = np.array(matrix)

cities= {"Home":True}
cities.update({chr(i):False for i in range(65, 64+matrix.shape[0])})

def find_next_city(current_city):
    current_city_index = list(cities.keys()).index(current_city)
    closest_city_distance = np.max(matrix)
    closest_city = ""
    for i in range(matrix.shape[0]):
        dist = matrix[current_city_index][i]
        city = list(cities.keys())[i]
        if dist != 0 and closest_city_distance > dist and cities[city] == False:
            closest_city_distance = dist
            closest_city = city
    cities[closest_city] = True
    print(f"Going to City {closest_city} from City {current_city}. The distance is {closest_city_distance} km.")
    if False in cities.values():
        find_next_city(closest_city)

while False in cities.values():
    find_next_city("Home")