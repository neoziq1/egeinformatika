for N in range(4, 100000):
    b = bin(N)[2: ]
    num = len(b)
    if num % 2 == 1:
        bit = str(1 - int(b[num // 2]))
        b = b[: num//2] + bit + b[num//2+1: ]
    else:
        bit = str(1 - int(b[num // 2 -1])) + str(1 - int(b[num // 2]))
        b = b[: num // 2] + bit + b[num//2+2: ]
    R = int(b, 2)
    if R > 100 and R < N:
        print(N)
        break
 а) если количество цифр в двоичной записи числа нечётное, то центральный бит двоичного представления инвертируется;
б) если количество цифр в двоичной записи числа чётное, то два центральных бита двоичного представления инвертируется;
Укажите минимальное число N, после обработки которого с помощью этого алгоритма получается число R, большее 100 и меньшее N. В ответе запишите это число в десятичной системе счисления.
