## 2. Array Comparisons ##

countries = world_alcohol[:,2]

countries_canada = (countries == "Canada")

years = world_alcohol[:,0]

years_1984 = (years == '1984')

## 3. Selecting Elements ##

print("oi")
countries = world_alcohol[:,2]
country_is_algeria = (countries == "Algeria")


print(country_is_algeria)

country_algeria1 = []

country_algeria = world_alcohol[country_is_algeria, :]

for i, country in enumerate(country_is_algeria):
    if country:
       country_algeria1.append(world_alcohol[i])
    
print(country_algeria)

## 4. Comparisons with Multiple Conditions ##

countries = world_alcohol[:,2]

years = world_alcohol[:,0]

is_algeria_and_1986 = (countries == "Algeria") & (years == "1986")

rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]


## 5. Replacing Values ##

years = world_alcohol[:,0]
is_1986 = (years == "1986")
world_alcohol[is_1986, 0] = "2014"

beverages = world_alcohol[:,3]
is_wine = (beverages == "Wine")
world_alcohol[is_wine, 3] = "Grog"


## 6. Replacing Empty Strings ##

display = world_alcohol[:,4]
is_value_empty = (display == "")

world_alcohol[is_value_empty, 4] = '0'

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:, 4]
alcohol_consumption = alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

countries = world_alcohol[:,2]
years = world_alcohol[:,0]

is_canada_1986 = (years == '1986') & (countries == 'Canada')
canada_1986 = world_alcohol[is_canada_1986,:]

print(canada_1986[:, 4])
is_value_empty = (canada_1986[:,4] == '')
canada_1986[is_value_empty, 4] = '0'
print(canada_1986[:, 4])
canada_alcohol = canada_1986[:,4].astype(float)

total_canadian_drinking = canada_alcohol.sum()



## 10. Calculating Consumption for Each Country ##

totals = {}

years = world_alcohol[:,0]
is1989 = (years=="1989")
year = world_alcohol[is1989,:]

is_empty = (year[:,4] == '')
year[is_empty,4] = '0'



for entry in year:
    if entry[2] in totals:
        totals[entry[2]] += float(entry[4])
    else:
        totals[entry[2]] = float(entry[4])

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None

for key in totals:
    if totals[key] > highest_value or highest_value == None:
        highest_value = totals[key]
        highest_key = key