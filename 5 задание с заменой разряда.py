for N in range(1, 36):
    b = bin(N)[2: ]
    if b.count('1') % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    R = int(b, 2)
    if R < 35:
        print(N)
