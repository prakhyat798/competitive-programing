# given array
arr = [1, 2, 3, 4, 5]
L = 2
R = 4
L = L - 1
R = R - 1
sum1 = 0
for i in range(L, R + 1):
    sum1 += arr[i]
print("sum of subarray:", sum1)
