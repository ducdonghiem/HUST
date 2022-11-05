def insertion_sort(lst):
    for j in range(1, len(lst)):
        current = lst[j]
        i = j - 1
        while i >= 0 and current < lst[i]:
            lst[i+1] = lst[i]
            i -= 1
        lst[i+1] = current
    return lst

def main():
    lst = [7, 5, 9, 2, 3, 1]
    print(insertion_sort(lst))

main()