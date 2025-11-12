
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
max_sum = arr[0]
curr_sum = 0
for i in range(n):  
    curr_sum += arr[i]  
    if curr_sum > max_sum:
        max_sum = curr_sum
    # if current sum goes below 0 then reset
    if curr_sum < 0:
        curr_sum = 0
print("maximum subarray sum:", max_sum)
