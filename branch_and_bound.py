import numpy as np
from backtracking import permutation

# traveling saleman problem (branch and bound)
class TSP():
    def candidate(c):
        n = len(c) - 1
        a = [0]*n
        lst = []
        permutation.Try(n)
        lst = permutation.result()
        return lst
    def solve(c):
        lst = TSP.candidate(c)
        # print(lst)
        min_cost = 100
        cost = 100
        quit = 1
        l = len(lst)
        minC = np.min(c[np.nonzero(c)])
        cities_num = len(lst[0]) + 1
        for i in range(l):
            if quit == 0 and cost < min_cost:
                min_cost = cost
            cost = 0
            k = 0
            lst[i].append(0)
            quit = 0
            for j in range(cities_num):
                cost += c[k][lst[i][j]]
                if cost + minC*(cities_num - 1 - j) > min_cost:
                    quit = 1
                    break
                k = lst[i][j]
        return min_cost

# knapsack problem
class knapsack():
    # bruteforce
    def brute_force_knapsack(k):
        for i in [1, 0]:
            x[k] = i
            cur_val = value.dot(x)
            cur_wei = weight.dot(x)
            # if cur_wei > capacity:
            #     continue
            if k == 3:
                if cur_wei <= capacity:
                    # val_lst.append(cur_val)
                    print(x, cur_val, cur_wei)
            else:
                knapsack.brute_force_knapsack(k+1)
    # branch and bound
    def branch_and_bound_knapsack(k):
        global valmax
        for i in [1, 0]:
            x[k] = i
            cur_val = value.dot(x)
            cur_wei = weight.dot(x)
            if k == 3:
                if cur_wei <= capacity:
                    if cur_val > valmax:
                        # print(valmax)
                        valmax = cur_val
                    print(x, valmax, cur_wei)
            else:
                if cur_val + (capacity - cur_wei)*value[k+1]/weight[k+1] < valmax:
                    continue
                else:
                    knapsack.branch_and_bound_knapsack(k+1)
        # return val_max


def main():
    C = np.array([[0, 4, 10, 2, 17],
                    [4, 0, 4, 11, 9],
                    [10, 4, 0, 12, 3],
                    [2 , 11, 12, 0, 13],
                    [17, 9, 3, 6, 0]])
    # C = np.array([[0, 3, 14, 18, 15],
    #             [3, 0, 4, 22, 20],
    #             [17, 9, 0, 16, 4],
    #             [9, 20, 7, 0, 18],
    #             [9, 15, 11, 5, 0]])
    
    print(TSP.solve(C))

    # Those value are ordered such that v/w decreases.
    global value, weight, capacity, x, valmax
    value = np.array([10, 5, 3, 6])
    weight = np.array([5, 3, 2, 4])
    capacity = 8
    x = np.array([0, 0, 0, 0])
    valmax = 0
    knapsack.brute_force_knapsack(0)
    print()
    knapsack.branch_and_bound_knapsack(0)
main()
