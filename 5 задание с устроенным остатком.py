for N in range(1, 61):
    b = bin(N)[2: ]
    if b.count('1') % 3 == 0:
        b += b[:2]
    else:
        b = bin((b.count('1') % 3) * 3) [2:] + b
    if int(b, 2) <= 60:
        print(N)
        
            
