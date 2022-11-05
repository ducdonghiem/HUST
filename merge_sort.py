def merge_sort(lst):
    length = len(lst)
    if length == 1:
        return lst
    mid = length // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    i = 0
    j = 0
    sorted = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted

def main():
    lst = [5 ,3, 7, 8, 4, 5]
    print(merge_sort(lst))

main()
