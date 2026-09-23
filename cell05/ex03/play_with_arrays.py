array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()

for number in array:
    if number > 5:
        new_array.add(number + 2)

print(array)
print(new_array)