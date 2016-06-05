from car import Car
from xml.dom import minidom
import json

json_open = open('5-main.json')
json_data = json_open.read()
data = json.loads(json_data)
json_open.close()

doc = minidom.Document()
cars = doc.createElement('cars')
doc.appendChild(cars)

brands = []
num_brands = 0
num_doors = 0

for f in data:
    car = Car(f)
    brands.append(car.get_brand())
    num_doors = (num_doors + car.get_nb_doors())
    car_xml = car.to_xml_node(doc)
    cars.appendChild(car_xml)

i = 0
len_brands = len(brands)
while i < len_brands:
    if brands[i] != brands[i -1]:
        num_brands += 1
    i += 1

print num_brands
print num_doors
print Car(data[3])
print doc.toxml(encoding='utf-8')

