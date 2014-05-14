import sys

############### Auxiliary functions #####################
def find_column_global_max(matrix, x, y0, y1):
    """ Finds global maximum of column x between rows y0 and y1 (inclusive). """
    best_y = y0
    best_h = matrix[x][best_y]
    for y in range(y0+1, y1+1):
        h = matrix[x][y]
        if best_h < h:
            best_y = y
            best_h = h
    return (x,best_y, best_h)            

def find_row_global_max(matrix, y, x0, x1):
    """ Finds global maximum of row y between columns x0 and x1 (inclusive). """
    best_x = x0
    best_h = matrix[best_x][y]
    for x in range(x0+1, x1+1):
        h = matrix[x][y]
        if best_h < h:
            best_x = x
            best_h = h
    return (best_x, y, best_h)            

def find_global_max(matrix, x0, x1, y0, y1):
    """ Finds global maximum of sub-matrix between columns x0 and x1 and rows y0 and y1 (inclusive). """
    best_x = x0
    best_y = y0
    best_h = matrix[best_x][best_y]
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            h = matrix[x][y]
            if(best_h < h):
                best_x = x
                best_y = y
                best_h = h
    return (best_x, best_y, best_h)

############################################################


####################### Algorithms Implementation #########################

"""Find a peak of a mountain range.

The mountain range is a 2-dimensional matrix of integers values,
indexed by closed intervals [x0,x1] and [y0,y1].

A peak is defined as a location which is at least as high as the adjacent
locations (two locations are adjacent if they share a common edge).

Keyword arguments:
matrix -- a matrix of altitudes
x0 -- an integer which is the leftmost index of the range
x1 -- an integer which is the rightmost index of the range
y0 -- an integer which is the bottom-most index of the range
y1 -- an integer which is the topmost index of the range

Return value: a pair of coordinates (x, y) of any local maximum location

"""

def quick_find_2d_peak(matrix, x0, x1, y0, y1):
    """
    Implement O(n) solution given in lecture.
    """
    
    ########### WRITE YOUR IMPLEMENTATION HERE ############
    mid = (x0 + x1) /2
    n = x1 - x0
    array = []
    m1 = find_column_global_max(matrix, y0, x0, x1)
    array.append(m1)
    m2 = find_column_global_max(matrix, mid, x0, x1)
    array.append(m2)
    m3 = find_column_global_max(matrix, y1, x0, x1)
    array.append(m3)

    
    m4 = find_row_global_max(matrix, x0, y0, y1)
    array.append(m4)
    m5 = find_row_global_max(matrix, mid, y0, y1)
    array.append(m5)
    m6 = find_row_global_max(matrix, x1, y0, y1)
    array.append(m6)

    array2 = []
    for arr in array:
        m = arr[2]
        array2.append(m)

    
    global_max = max(array2)
    max_ind = array[array2.index(global_max)]
    (i,j) = (max_ind[0], max_ind[1])

    # most left column
    if (i == x0):
        if (matrix[x0][j] >= matrix[x0+1][j]):
            return (i, j)
        
        else:
            if (j >= mid) :
                return quick_find_2d_peak(matrix, x0, mid, mid, y1)
            else:
                return quick_find_2d_peak(matrix, x0, mid, y0, mid)
            
    # bottom row       
    elif (j == y0):
        if (matrix[i][y0] >= matrix[i][y0 + 1]):
            return (i, j)
        
        
        else:
            if i >= mid:
                return quick_find_2d_peak(matrix, mid, x1, y0, mid)
            else:
                return quick_find_2d_peak(matrix, x0, mid, y0, mid)

    # most right column
    elif (i == x1):
        if (matrix[x1][j] >= matrix[x1 - 1][j]):
            return (i, j)
        
            
        else:
            if j >= mid:
                return quick_find_2d_peak(matrix, mid, x1, mid, y1)
            else:
                return quick_find_2d_peak(matrix, mid, x1, y0, mid)

    # most upper row
    elif (j == y1):
        if (matrix[i][y1] >= matrix[i][y1 - 1]):
            return (i, j)
        
    
        else:
            if i >= mid:
                return quick_find_2d_peak(matrix, mid, x1, mid, y1)
            else:
                return quick_find_2d_peak(matrix, x0, mid, mid, y1)
            
    # middle column
    elif (i== mid):
        if (matrix[mid][j] >= matrix[mid- 1][j]) and (matrix[mid][j] >= matrix[mid + 1][j]) :
            return (i, j)
        
       
        else:
            if matrix[mid + 1][j] > matrix[mid][j]:
                if j >= mid: return quick_find_2d_peak(matrix, mid, x1, mid, y1)
                else:
                    return quick_find_2d_peak(matrix, mid, x1, y0, mid)

            elif matrix[mid - 1][j] > matrix[mid][j]:
                if j >= mid:
                    return quick_find_2d_peak(matrix, x0, mid, mid, y1)
                else:
                    return quick_find_2d_peak(matrix, x0, mid, y0, mid)
                
    # middle row
    elif (j == mid):
        if (matrix[i][mid] >= matrix[i][mid + 1]) and (matrix[i][mid] >= matrix[i][mid- 1]):
            return (i, j)
        
   
        else:
            if matrix[i][mid + 1] > matrix[i][mid]:
                if i >= mid:
                    return quick_find_2d_peak(matrix, mid, x1, mid, y1)
                else:
                    return quick_find_2d_peak(matrix, x0, mid, mid, y1)
            elif matrix[x][mid - 1] > matrix[x][mid]:
                if i >= mid:
                    return quick_find_2d_peak(matrix, mid, x1, y0, mid)
                else:
                    return quick_find_2d_peak(matrix, x0, mid, y0, mid)
                
        
            
    
    return (x0, y0) # Change this to return your solution.
    #######################################################


def medium_find_2d_peak(matrix, x0, x1, y0, y1):
    """
    Implements O(n log(n)) solution given in lecture.
    """
    
    while x0 < x1: 

        mid_x = (x0+x1)/2 # If the width of the range is even,
                          # this picks the cell slightly to the left of the middle
 
        mid_col_glob_max = find_column_global_max(matrix, mid_x, y0, y1)
        right_col_glob_max = find_column_global_max(matrix, mid_x + 1, y0, y1)

        if right_col_glob_max[1] > mid_col_glob_max[1]:
            x0 = mid_x + 1 # choose the right half
        else:
            x1 = mid_x # choose the left half
             
    max_y_and_value = find_column_global_max(matrix, x0, y0, y1)
    return (x0, max_y_and_value[0])


def slow_find_2d_peak(matrix, x0, x1, y0, y1):
    """
    Implements O(n^2) solution given in lecture.
    """
    result = find_global_max(matrix, x0, x1, y0, y1)
    return (result[0], result[1])
##########################################################################
