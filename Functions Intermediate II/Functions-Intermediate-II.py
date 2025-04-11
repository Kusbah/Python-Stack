
import random

# 1. Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Make the updates
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

# 2. Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for student in some_list:
        output = []
        for key, value in student.items():
            output.append(f"{key} - {value}")
        print(", ".join(output))

# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        if key_name in item:
            print(item[key_name])

# 4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key in some_dict:
        values = some_dict[key]
        print(f"{len(values)} {key.upper()}")
        for item in values:
            print(item)
        print()

# Example data
students = [
    {'first_name': 'Michael', 'last_name': 'Bryant'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# Run functions to show results
print("Updated Structures:")
print(x)
print(students)
print(sports_directory)
print(z)

print("\nIterate Dictionary:")
iterateDictionary(students)

print("\nFirst Names:")
iterateDictionary2('first_name', students)

print("\nLast Names:")
iterateDictionary2('last_name', students)

print("\nPrint Info:")
printInfo(dojo)
