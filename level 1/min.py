numbers = [4, 7, 2, 9, 1]
min=numbers[0]
for i in range(1,len(numbers)):
    if numbers[i]<min:
        min=numbers[i]
print(min)