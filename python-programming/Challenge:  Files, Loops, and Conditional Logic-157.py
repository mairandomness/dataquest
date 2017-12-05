## 3. Read the File Into a String ##

r = open("dq_unisex_names.csv", "r")
names = r.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
nested_list = []
names_list = names.split('\n')
for name in names_list:
    nested_list.append(name.split(','))
print(nested_list[0:5])



## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list =nested_list[:]
for numb in numerical_list:
    numb[1]= float(numb[1])
print(numerical_list[0:5])
    


## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for name in numerical_list:
    if name[1] >= 1000:
        thousand_or_greater.append(name[0])
print(thousand_or_greater[0:10])
