## 2. Sets ##

import csv

f = open("legislators.csv")
r = csv.reader(f)
legislators = list(r)
legislators = legislators[1:]
gender = []
for person in legislators:
    gender.append(person[3])
gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

import csv

f = open("legislators.csv")
r = csv.reader(f)
legislators = list(r)
legislators = legislators[1:]
party = []
for person in legislators:
    party.append(person[6])
party = set(party)
print(party)

## 4. Missing Values ##

import csv

f = open("legislators.csv")
r = csv.reader(f)
legislators = list(r)
legislators = legislators[1:]
gender = []
for person in legislators:
    if person[3] == '':
        person[3] = 'M'
    gender.append(person[3])
gender = set(gender)
print(gender)

## 5. Parsing Birth Years ##

import csv

f = open("legislators.csv")
r = csv.reader(f)
legislators = list(r)
legislators = legislators[1:]
birth_years = []
for person in legislators:
    if person[3] == '':
        person[3] = 'M'
    birth_years.append((person[2].split('-'))[0])
#birth_years = set(birth_years)
print(birth_years)

## 6. Try/except Blocks ##

a = "hello"

try:
    float(a)
except:
    print("Error converting to float.")

## 7. Exception Instances ##

a = ""

try:
    float(a)
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
import csv

f = open("legislators.csv")
r = csv.reader(f)
legislators = list(r)
legislators = legislators[1:]
birth_years = []
for person in legislators:
    if person[3] == '':
        person[3] = 'M'
    birth_years.append((person[2].split('-'))[0])
#birth_years = set(birth_years)
for year in birth_years:
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)

## 9. Convert Birth Years to Integers ##

converted_years = []
import csv

f = open("legislators.csv")
r = csv.reader(f)
legislators = list(r)
legislators = legislators[1:]
birth_years = []
for person in legislators:
    if person[3] == '':
        person[3] = 'M'
    birth_year = (person[2].split('-'))[0]
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
    person.append(birth_year)


## 10. Fill in Years Without a Value ##

last_value = 1

for person in legislators:
    if person[7] == 0:
        person[7] = last_value
    last_value = person[7]
        