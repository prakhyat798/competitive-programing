n = int(input())

for i in range(1, n+1):
    print("*", end=" ")
    for j in range(n+1):
        print("-", end=" ")
    print("*", end=" ")
    print()
