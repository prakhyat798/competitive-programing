# given array
arr = [1, 2, 3]
n = len(arr)
print("sum of all subarrays:\n")
for i in range(n):
    sum1 = 0
    for j in range(i, n):
        sum1 += arr[j]
        print(sum1)
