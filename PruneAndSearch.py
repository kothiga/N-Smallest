import numpy as np

def SortAndSearch(values, k):
    if k > len(values): return np.inf
    sorted_values = np.sort(values)
    return sorted_values[k-1]


def _median(values):
    return np.sort(values)[len(values)//2]


def _findIdx(values, v):
    idx = 0
    for val in values:
        if v == val: return idx
        idx += 1
    return idx


def _partition(values, pivotValue):

    # Get the length of our array.
    n = len(values)-1

    # Find the position the values up to last element.
    pos = 0 if n == 0 else _findIdx(values, pivotValue)
    
    # Swap this position with the last position.
    values[pos], values[-1] = values[-1], values[pos]

    # Do a fast partition on the values.
    idx0 = 0
    for idx1 in range(n):
        if values[idx1] < pivotValue:
            values[idx0], values[idx1] = values[idx1], values[idx0]
            idx0 += 1
    
    values[idx0], values[-1] = values[-1], values[idx0]
    
    # Return the index of the first instance of pivotValue.
    return idx0


def PruneAndSearch(values, k):

    # Get the length of our array.
    n = len(values)
    
    # Base Case. No work to be done.
    if n == 1: return values[0]
    
    # Group the original list into subsets of 5, 
    # and find the median of those values.
    medianValues = [ _median(values[ idx : idx+5 ]) for idx in range( 0, n, 5 ) ]
    m = len(medianValues)

    # Find the Median-of-Medians . . .
    median = medianValues[0] if m == 1 else PruneAndSearch( medianValues, m // 2 )

    # . . . And use this value to pivot on for a partition.
    pos = _partition(values, median)

    # Recurse further down pruning either the 
    # left or right side. If our pivot position is
    # the k-th value we are looking for, return it. 
     
    if pos == k-1: return values[pos]
    if pos >  k-1: return PruneAndSearch(values[ : pos ], k)
    #  pos <  k-1
    return PruneAndSearch(values[ pos+1 : ], k-pos-1)

