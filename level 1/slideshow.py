numbers = [3, 7, 2, 9, 5, 8]
k = 3
window_sum=0
for i in range(k):
    window_sum=window_sum+numbers[i]
print(window_sum)
for i in range(k,len(numbers)):
    window_sum=window_sum-numbers[i-k]
    window_sum=window_sum+numbers[i]
    print(window_sum)