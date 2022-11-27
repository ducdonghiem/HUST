# T(n) = O(n)
def findk(lst, k):
    for i in range(len(lst)):
        if lst[i] == k:
            return i
    return -1


# T(n) = T(n/2) + 1 = O(logn) with T(1) = 2.
# This is better than looking through every element to find k which causing T(n) = O(n).

def binary_search(lst, k, low, high):      
    if low <= high:
        mid = (high + low) // 2
        if lst[mid] == k:
            return mid
        else:
            if lst[mid] > k:
                return(binary_search(lst, k, low, mid))
            else:
                return(binary_search(lst, k, mid + 1, high))
    else:
        return -1

def main():
    lst = [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97]
    # lst = [95]
    print(binary_search(lst, 33, 0, len(lst) - 1))
    print(findk(lst, 33))
main()



