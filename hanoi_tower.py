def hanoi_tower(n, a, b, c):   # T(n) = 2^n - 1 = O(2^n)
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi_tower(n-1, a, c, b)
        print(a, '-->', c)
        hanoi_tower(n-1, b, a, c)

hanoi_tower(3, 'A', 'B', 'C')
