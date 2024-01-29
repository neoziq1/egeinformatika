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
Алгоритм получает на вход натуральное число N ≥ 10 и строит по нему новое число R следующим образом:
1) Все пары соседних цифр в десятичной записи N рассматриваются как двузначные числа (возможно, с ведущим нулём).
2) Из списка полученных на предыдущем шаге двузначных чисел выделяются наименьшее и наибольшее.
3) Результатом работы алгоритма становится сумма найденных на предыдущем шаге двух чисел.
При каком наименьшем N в результате работы алгоритма получится R = 137?
