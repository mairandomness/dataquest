## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, thing in enumerate(things):
    thing.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = []
apple_prices_lowered = []

for apple in apple_prices:
    apple_prices_doubled.append(apple * 2)
    apple_prices_lowered.append(apple - 100)

## 5. Counting Female Names ##

name_counts = {}
for person in legislators:
    if person[3] == "F" and person[7] > 1940:
        name = person[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

for value in values:
    if value == None or value <= 30:
        checks.append(False)
    else:
        checks.append(True)
        
    

## 8. Highest Female Name Count ##

max_value = None
for key in name_counts:
    count = name_counts[key]
    if max_value == None or count > max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for plant, value in plant_types.items():
    print(plant)
    print(value)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for key, value in name_counts.items():
    if value == 2:
        top_female_names.append(key)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts = {}
for person in legislators:
    if person[3] == "M" or person[7] > 1940:
       if person[1] in male_name_counts:
          male_name_counts[person[1]] += 1
       else:
          male_name_counts[person[1]] = 1
high = None
for key,value in male_name_counts.items():
    if high == None or value > high:
        high = value
for key,value in male_name_counts.items():
    if high == value:
        top_male_names.append(key)
     