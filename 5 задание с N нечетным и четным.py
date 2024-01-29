res = set()
for N in range(1, 191):
    b = bin(N)[2: ]
    if N % 2 == 0:
        b = '1' + b + '00'
    else:
        b += bin(b.count('1'))[2:]
    R = int(b, 2)
    if R > 190:
        res.add((R, N))
print(sorted(res))
