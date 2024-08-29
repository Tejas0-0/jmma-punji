# ques-1  Write a Python program to sum all the items in a list.
my_list = [1, 2, 3, 4, 5]
result = sum(my_list)
print("The sum of the list is:", result)


# ques-2  Write a Python program to traverse a given list in reverse order, and print the elements with the original index. Original list: ['red', 'green', 'white', 'black'] Traverse the said list in reverse order: black white green red
my_list = ['red', 'green', 'white', 'black']

print("Original list:", my_list)
print("Traverse the list in reverse order:")
for i, elem in enumerate(reversed(my_list)):
    print(f"Index: {i}, Element: {elem}")


# ques-3 Write a Python program to get the largest and smallest number from a list without builtin functions.
def find_largest_smallest(lst):
    largest = lst[0]
    smallest = lst[0]

    for num in lst:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest

# Test the function
numbers = [12, 45, 7, 23, 56, 89, 34]
largest, smallest = find_largest_smallest(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)


#ques-4 Write a Python program to find duplicate values from a list and display those.
def find_duplicates(lst):
    duplicates = []
    for num in lst:
        if lst.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    return duplicates

# Test the function
numbers = [1, 2, 3, 4, 2, 7, 8, 8, 9]
duplicates = find_duplicates(numbers)

print("Duplicate values:", duplicates)


# ques-5 Write a Python program to split a given list into two parts where the length of the first part of the list is given. Original list: [1, 1, 2, 3, 4, 4, 5, 1] Length of the first part of the list: 3 Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_first_part = 3

first_part = original_list[:length_first_part]
second_part = original_list[length_first_part:]

print("Original list:", original_list)
print("Length of the first part of the list:", length_first_part)
print("Splitted list into two parts:", (first_part, second_part))
