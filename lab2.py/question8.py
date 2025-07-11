all_rolls = set(input("Enter roll numbers of all students separated by space: ").split())
cricket_rolls = set(input("Enter roll numbers of cricket players separated by space: ").split())
football_rolls = set(input("Enter roll numbers of football players separated by space: ").split())

print("Students who play both sports:", (cricket_rolls & football_rolls))
print("Students who play only one sport:", (cricket_rolls ^ football_rolls))
print("Students who play neither sport:", (all_rolls - (cricket_rolls | football_rolls)))
