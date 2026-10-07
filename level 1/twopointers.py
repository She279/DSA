numbers = [2, 4, 6, 8, 10, 12]
target = 14
left=0
right=len(numbers)-1
while left<right:
    total=numbers[left]+numbers[right]
    if total==target:
        print("found",numbers[left],numbers[right])
        break
    elif total<target:
        left=left+1
    else:
        right=right-1