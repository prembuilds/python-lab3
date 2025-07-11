
n = int(input("Enter number of elements: "))
numbers = []

print("Enter the numbers:")
for _ in range(n):
    num = int(input())
    numbers.append(num)

print("\nOriginal List:", numbers)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

sorted_list = sorted(numbers)
print("Sorted List:", sorted_list)

no_duplicates = list(set(numbers))
print("List without Duplicates:", no_duplicates)

max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print("Maximum:", max_num)
print("Minimum:", min_num)


unsorted = numbers[:]
for i in range(len(unsorted)):
    for j in range(len(unsorted) - i - 1):
        if unsorted[j] > unsorted[j + 1]:
            unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
print("Sorted List:", unsorted)

unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print("List without Duplicates:", unique_list)
