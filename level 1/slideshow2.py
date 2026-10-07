numbers = [4, 2, 10, 3, 8, 6, 1]
k = 3
window_sum=0
for i in range(k):
    window_sum=window_sum+numbers[i]
max=window_sum
for i in range(k,len(numbers)):
    window_sum=window_sum-numbers[i-k]
    window_sum=window_sum+numbers[i]
    if window_sum>max:
        max=window_sum
print(max)