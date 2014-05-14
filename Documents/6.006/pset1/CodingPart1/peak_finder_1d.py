def quick_find_1d_peak(array):
    """Finds a peak of a mountain range.

    The mountain range is a 1-dimensional array of values. A peak is
    defined as a location which is at least as high as the adjacent
    locations. Returns the index in the array of some peak.

    Keyword arguments:
    array -- an array containing the values

    returns the location x0 of the peak

    """

    ############## IMPLEMENT the O(log n) time algorithm here ############
    return peak_finder(array, 0, len(array)-1)        


def peak_finder(array, x, y):
    x0 = 1
    n = len(array)
    mid = n/2
    mid_num = array[mid]

    if ( y == x+1 ):
        if array[x] >= array[y]:
            return x
        else: return y

    if (array[mid-1] <= array[mid]) and (array[mid+1] <= array[mid]):
        return mid

    
    if mid+1 < n and mid-1 > 0:
        if mid_num >= array[mid+1] and mid_num >= array[mid-1]:
            #print "This is the middle " + str(mid)
            #print array[mid]
            return mid
        elif mid_num < array[mid+1]:
            #print "right: " + str(mid_num)
            #print n
            return quick_find_1d_peak(array[(mid+1):])
        elif mid_num < array[mid-1]:
            #print "left: " + str(mid_num)
            return quick_find_1d_peak(array[0:mid])

    elif mid+1 >= n:
        #print "This is the end " + str(n)
        #print array[n-1]
        return mid
    elif mid-1 <= 0:
        #print 0
        return 0




    
    ##################################################################

def slow_find_1d_peak(array):
    best_x = 0
    best_h = array[0]
    for x in range(1, len(array)):
        h = array[x]
        if best_h < h:
            best_x = x
            best_h = h
    return best_x
