#!/bin/python3

   def bsmin(lo, hi, f):
  1     if not f(hi): return "oof"
  2     assert hi >= lo
  3     while lo < hi:
  4         mid = lo + (hi - lo) // 2
  5
  6         if f(mid):
  7             hi = mid
  8         else:
  9             lo = mid + 1
 10
 11     return lo

def bsMax(): pass

def bsArr(): pass

