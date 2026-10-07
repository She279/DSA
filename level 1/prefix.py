numbers = [5, 10, 15, 20, 25]
prefix=[]
total=0
for num in numbers:
    total=total+num
    prefix.append(total)
print("prefix sum=",prefix)