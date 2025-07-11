list1 = []
number1 = int(input("How many elements you want to add in the list1?"))
for _ in range(number1):
    temp = int(input("Enter the elements: "))
    list1.append(temp)

list2 = []
number2 = int(input("How many elements you want to add in the list2?"))
for _ in range(number2):
    temp = int(input("Enter the elements: "))
    list2.append(temp)

common_elements = []

for value in list1:
    if value in list2 and value not in common_elements:
        common_elements.append(value)
    
merged_list = list1 + list2

final_list = []
for value in merged_list:
    if value not in common_elements:
        final_list.append(value)

print(f"Original List1 : {list1}")
print(f"Original list2 : {list2}")
print(f"List with common elements : {common_elements}")
print(f"Merged list : {final_list}")
