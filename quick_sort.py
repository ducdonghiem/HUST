# lst = input().split(' ')
# for i in range(len(lst)):
#     lst[i] = int(lst[i])


def quick_sort(lst, low, high):
    # i = low
    # if low > high:
        
    if low < high:
        i = low
        pivot = lst[high]
        for j in range(low ,high):
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
        lst[i], lst[high] = lst[high], lst[i]
        pivot_index = i
        quick_sort(lst, low, pivot_index-1)
        quick_sort(lst, pivot_index+1, high)
    
def main():
    lst = [5, 7, 2, 3, 1]
    quick_sort(lst, 0, len(lst)-1)
    print(lst)

main()

    
