size = int(input("How many numbers will you enter? "))
nums = []
for i in range(size):
    val = int(input(f"Enter element {i + 1}: "))
    nums.append(val)

num_tuple = tuple(nums)
mean = sum(num_tuple) / len(num_tuple)
print("Average:", mean)

sorted_nums = sorted(num_tuple)
length = len(sorted_nums)

if length % 2 == 0:
    mid1 = sorted_nums[length // 2 - 1]
    mid2 = sorted_nums[length // 2]
    med = (mid1 + mid2) / 2
else:
    med = sorted_nums[length // 2]

print("Median:", med)

unique_vals = tuple(set(num_tuple))
freq_list = []
for value in unique_vals:
    count = 0
    for item in num_tuple:
        if item == value:
            count += 1
    freq_list.append(count)

highest = freq_list[0]
mode_index = 0
for i in range(1, len(freq_list)):
    if freq_list[i] > highest:
        highest = freq_list[i]
        mode_index = i

print("Mode:", unique_vals[mode_index])
