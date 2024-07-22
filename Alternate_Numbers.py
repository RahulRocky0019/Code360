from typing import *

def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    result = [0] * len(a)
    pos, neg = 0, 1
    for i in a:
        if i >= 0:
            result[pos] = i
            pos += 2
        else:
            result[neg] = i
            neg += 2
    
    return result
