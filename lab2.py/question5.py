n = int(input("Enter the number of elements: "))
list1 = []
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    list1.append(num)

list2 = []
for index in range(0, len(list1), 2):
    number = list1[index]
    if number > 1:
        count = 0
        for j in range(1, number + 1):
            if number % j == 0:
                count += 1
        if count == 2:
            list2.append(number)

print(list2)
