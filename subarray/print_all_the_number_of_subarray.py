# array already given (no input needed)
arr = [1, 2, 3, 4, 5]

n = len(arr)

print("All subarrays are:\n")

for i in range(n):
    
    for j in range(i, n):
        
        # print elements from i to j in same line
        for k in range(i, j + 1):
            print(arr[k], end=" ")
        
        print()    # move to next line
