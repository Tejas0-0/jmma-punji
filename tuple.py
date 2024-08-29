'''
ques-1
write a python program to find the numbers of times 4 appears in the tuple. 
input: tuplex=(2,4,5,6,2,3,4,4,7) 
output:3
'''
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)

count = tuplex.count(4)

print("The number 4 appears", count, "times in the tuple.")


'''
ques-2
write a python program to convert a list to a tuple.
input: listx=[5,10,7,4,15,3]
output: (5,10,7,4,15,3)
'''
listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)

print("The tuple is:", tuplex)


'''
ques-3
write a python program to calculate the sum of the numbers in a given tuple. 
input: tuples_list=[(1,2), (3,4), (5,6)] 
output: Sum of values in the tuples: 21
'''
tuples_list = [(1,2), (3,4), (5,6)]

sum_of_values = 0
for tup in tuples_list:
    for val in tup:
        sum_of_values += val

print("Sum of values in the tuples:", sum_of_values)


'''
ques-4
write a python program and iterate the given tuples 
input: 
employee1=("John Doe", 101, "Human Resources", 60000) 
employee2=("Alice Smith", 102, "Marketing", 55000) 
employee3= ("Bob Johnson", 103, "Engineering", 75000) 

output: 
Employee Records: 
Name: John Doe 
Employee ID: 101 
Department: Human Resources 
Salary: $60000

Name: Alice Smith 
Employee ID: 102 
Department: Marketing 
Salary: $55000

Name: Bob Johnson 
Employee ID: 103 
Department: Engineering 
Salary: $75000
'''
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

employees = [employee1, employee2, employee3]

print("Employee Records:")

for employee in employees:
    print("Name:", employee[0])
    print("Employee ID:", employee[1])
    print("Department:", employee[2])
    print("Salary: $", employee[3])
    print()