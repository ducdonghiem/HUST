# brute force with improvement(go through each element once): T = n^2/2 + n/2 = O(n^2)
def bfi(lst):
    l = len(lst)
    max_sum = 0
    for i in range(l):
        sum = 0
        for j in range(i, l):
            sum += lst[j]
            if sum > max_sum:
                max_sum = sum 
    return max_sum

# using recursion by dividing the set by 2: T = O(nlogn)

class divide_and_conquer():
    def maxsub(lst):
        if len(lst) == 1:
            return lst[0]
        else:
            mid = len(lst)//2
            left = divide_and_conquer.maxsub(lst[:mid])
            right = divide_and_conquer.maxsub(lst[mid:])
            middle = divide_and_conquer.maxleft(lst[:mid]) + divide_and_conquer.maxright(lst[mid:])
            ans = max(left, middle, right)
            return ans
    def maxright(lst):
        sum = 0
        max_sum = -100
        for i in range(len(lst)):
            sum += lst[i]
            if sum > max_sum:
                max_sum = sum
        return max_sum
    def maxleft(lst):
        sum = 0
        max_sum = -100
        for i in range(len(lst) - 1 , -1, -1):
            sum += lst[i]
            if sum > max_sum:
                max_sum = sum
        return max_sum 

# dynamic programming considers the relation between n and n-1. 

class dynamic_programming():

# This is my code basing on my understanding. Dunno what the time complexity is.

    def maxsub(lst):
        if len(lst) == 1:
            return lst[0]
        else:
            return max(dynamic_programming.maxsub(lst[:-1]), lst[-1], dynamic_programming.end(lst[:-1]) + lst[-1])
    def end(lst):
        sum = 0
        max_sum = -100
        for i in range(len(lst)-1, -1, -1):
            sum += lst[i]
            if sum > max_sum:
                max_sum = sum
        return max_sum

# this is the best with T = O(n)

    def maxsubest(lst):
        smax = lst[0]
        ei = lst[0]
        # imax = 0
        for i in range(1, len(lst)):
            ei = max(lst[i], ei + lst[i])
            smax = max(smax, ei)
            # u = ei + lst[i]
            # v = lst[i]
            # if u > v:
            #     ei = u
            # else:
            #     ei= v
            # if ei > smax:
            #     smax = ei
            #     imax = i
        return smax

def main():
    lst = [-2, 11, -4, 13, -5, 2]
    print(bfi(lst))
    print(divide_and_conquer.maxsub(lst))
    print(dynamic_programming.maxsub(lst))
    print (dynamic_programming.maxsubest(lst))

main()


