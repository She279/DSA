num=[10,5,6,12,15,20]
largest=num[0]
for i in range(len(num)):
    if num[i]>largest:
        largest=num[i]
print(largest)