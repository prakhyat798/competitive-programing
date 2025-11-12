arr = [1, 2, 3, 4]
n = len(arr)
print("total subarrays:", n * (n + 1) // 2)
print("subarrays are:")
for i in range(n):
    for j in range(i, n):  
        print(arr[i:j+1])
