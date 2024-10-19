#!/bin/python3

def bsmin(lo, hi, f):
    assert hi >= lo
    if not f(hi): return "404"
    while lo < hi:
        mid = lo + (hi - lo) // 2

    if f(mid):
        hi = mid
    else:
        lo = mid + 1
        return lo

def bsMax(lo, hi, f):
    assert hi >= lo
    if not f(lo): return "404"
    while lo < hi:
        mid = lo + (hi - lo) // 2

        if f(mid):
            lo = mid
        else:
            hi = mid - 1
    return hi

def bsArr(arr, val):
    lo = 0
    hi = len(arr)
    
    while lo < hi:
        mid = lo + (lo + hi) // 2

        if arr[mid] < val:
            lo = mid
        elif arr[mid] > val:
            hi = mid
        else:
            return arr[mid]

    return "404"
