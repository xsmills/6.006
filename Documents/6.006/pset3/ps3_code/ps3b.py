# heap_sort() returns a copy of list A sorted in descending order.
# For example, heapsort([4,8,3,6]) should return [8,6,4,3].
# heap_sort() should NOT modify the list A.

def siftDown(A, start, end):

    root = start

    while root*2 + 1 <= end:
        child = root *2 + 1
        swap = root

        if A[swap] < A[child]:
            swap = child

        if child < end and A[swap] < A[child+1]:
            swap = child + 1

        if swap != root:
            temp = A[root]
            A[root] = A[swap]
            A[swap] = temp
            root = swap

        else:
            return

def heapify(A, count):
    start = count/2 - 1

    while start >= 0:
        ## sift down the node at index start to the proper
        ##

        siftDown(A, start, count - 1)
        start -= 1
    return



def heap_sort(a):
    # YOUR CODE HERE
    A = a[:]
    count = len(A)
    heapify(A, count)

    end = count - 1
    while end > 0 :
        ### swap the root(maximum value) of the heap with the last
        temp = A[0]
        A[0] = A[end]
        A[end] = temp

        siftDown(A, 0, end-1)
        ## decrease the size of the heap by one so that the previous
        ##

        end -= 1

   
    return A


    



    
        
    

    
    
   
    
        
    

# This function takes a list which contains the daily penalties for
# each problem set, and returns the smallest total penalty Ben can
# achieve. You should use your heap_sort() implementation.
def best_score(penalties):
    # YOUR CODE HERE
    min_penalties = []
    penalties_list = heap_sort(penalties)
    i = len(penalties_list)
    for p in penalties_list:
        min_penalties.append(p*i)
        i -= 1
    return sum(min_penalties)
        
