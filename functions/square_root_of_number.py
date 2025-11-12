def check_square(num):
    sq = num ** 0.5
    if int(sq) == sq:
        return int(sq)
    else:
        return -1
a = 49
print(check_square(a))
