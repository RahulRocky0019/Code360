def getFloorAndCeil(a, n, x):
    # Write your code here.

    low, high = 0, n - 1
    floor, ceil = float('-inf'), float('inf')

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == x:
            return [x, x]
        elif a[mid] < x:
            low = mid + 1
            floor = max(floor, a[mid])
        else:
            high = mid - 1
            ceil = min(ceil, a[mid])
    
    if floor == float('-inf'):
        floor = -1
    if ceil == float('inf'):
        ceil = -1
    
    return [floor, ceil]

