for N in range(1, 76):
    b = bin(N)[2: ]
    if N % 3 == 0:
        b += b[-3: ]
    else:
        b += bin((N % 3) * 3)[2: ]
    if int(b, 2) < 76:
        print(N)
