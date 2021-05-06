# Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15.
x[1][0] = 15
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"]="Bryant"
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0]="Andres"
# Change the value 20 in z to 30
z[0]["y"]=30

# Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for student in students:
        print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")

# Get Values From a List of Dictionaries
def iterateDictionary(key_name, some_list):
    for key in some_list:
        print(key[key_name])

# Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key,value in some_dict.items():
        print(f"{len(value)} {key}")
        for x in value:
            print(x)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
