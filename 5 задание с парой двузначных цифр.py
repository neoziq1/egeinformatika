for N in range(10, 10000):
    if N < 100:
        continue

    elif N < 1000:
        s = str(N)
        a, b = int(s[:2]), int(s[-2:])
        if a + b == 137:
            print(N)
            break

        else:
            s = str(N)
            nums = int(s[2:]), int(s[1:3]), int(s[-2:])
            if min(nums) + max(nums) == 137:
                print(N)
                break
