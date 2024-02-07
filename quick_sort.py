def quickSort(n):
    if len(n)<=1:
        return n
    pivot=n[len(n)//2]

    left=[x for x in n if x<pivot]
    middle=[x for x in n if x==pivot]
    right=[x for x in n if x>pivot]

    return quickSort(left)+middle+quickSort(right)
print(quickSort([12, 4, 5, 6, 7, 3, 1, 15]))
