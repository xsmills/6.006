from array import array

# An alternative to Python's dict class.
class Footable:
    # Creates a new hashtable.
    def __init__(self):
        self.tablesize = 32
        self.data = [None] * self.tablesize
        return
    # Inserts v into the hashtable with the key k.  Raises KeyError if
    # the key k already has a value associated with it.
    def put(self, k, v):
        assert int == type(k) and k >= 0
        if None != self.data[k % self.tablesize]:
            raise KeyError
        self.data[k % self.tablesize] = v
        return
    # Removes the element with key k if it exists; raises KeyError if
    # it does not.
    def remove(self, k):
        assert int == type(k) and k >= 0
        if None == self.data[k % self.tablesize]:
            raise KeyError
        self.data[k % self.tablesize] = None
        return
    # Returns the element with key k if it exists; raises KeyError if
    # it does not.
    def get(self, k):
        assert int == type(k) and k >= 0
        val = self.data[k % self.tablesize]
        if None == val:
            raise KeyError
        return val


class FootableLinear(Footable):
    def __init__(self):
        return Footable.__init(self)

    
    def put(self, k, v):
        assert int == type(k) and k >= 0
        if None == self.data[k % self.tablesize]:
            self.data[k % self.tablesize] = (k,v)
        else:
            i = 0
            m = self.tablesize
            ## keep probing till empty space is found
            for j in self.data:
                if self.data[(k % m + i) % m ] == None:
                    self.data[(k % m + i) % m] = (k,v)
                    return
                else:
                    i += 1
            
        return

    def remove(self, k):
        assert int == type(k) and k >= 0
        if k == self.data[k % self.tablesize][0]:
            self.data[k % self.tablesize] = None
        else:
            i = 0
            m = self.tablesize
            for j in self.data:
                if self.data[(k % m + i) % m][0] == k:
                    ## leave a DEL marker
                    self.data[(k % m + i) % m] = None
                    return
                else:
                    i += 1             
        return 

    def get(self, k):
        assert int == type(k) and k >= 0
   
        if self.data[k % self.tablesize][0] == k:
            return self.data[k % self.tablesize]
        elif self.data[k % self.tablesize][0] != k:
            i = 0
            m = self.tablesize
            for j in self.data:
                if self.data[(k % m + i) % m][0] == k:
                    return self.data[(k % m + i) % m ]
                else:
                    i += 1
        return

    ## Testing the Linear probing hash function
    ## leads to infinite loop where value cannot be found
    def badLinear(self):
        self.data = [2] * self.tablesize
        return self.get(4000)


class FootableChaining(Footable):
    def __init__(self):
        return Footable()

    def put(self, k, v):
        assert int == type(k) and k >= 0
        if None == self.data[k % self.tablesize]:
            ## store each value as a list
            self.data[k % self.tablesize] = []
            self.data[k % self.tablesize].append([k,v])

        else:
            self.data[k % self.tablesize].append([k,v])                    
        return

    def remove(self, k):
        assert int == type(k) and k >= 0
        if k == self.data[k % self.tablesize][0]:
            self.data[k % self.tablesize] = None
        else:
            for v in self.data[k % self.tablesize]:
                if v[0] == k:
                    self.data[k % self.tablesize].remove(v)
        return

    def get(self, k):
        assert int == type(k) and k >= 0
        val = self.data[k % self.tablesize]
        if val[0] == k:
            return val[1]
        else:
            for v in self.data[k % self.tablesize]:
                if v[0] == k:
                    return v[1]

        return
            
        
        
        




class FootableDouble(Footable):
    def __init__(self):
        return Footable.__init(self)

    
    def put(self, k, v):
        assert int == type(k) and k >= 0
        i = 0
        m = self.tablesize
        if None == self.data[((k % m) + (1 + (k % m-1)) * i) % m]:
            self.data[((k % m) + (1 + (k % m-1)) * i) % m] = (k,v)
        elif "DEL" == self.data[((k % m) + (1 + (k % m-1)) * i) % m][1]:
            self.data[((k % m) + (1 + (k % m-1)) * i) % m] = (k,v)
        else:
            ## keep probing till empty space is found
            ## using double hashing 
            for j in self.data:
                if self.data[((k % m) + (1 + (k % m-1)) * i) % m] == None:
                    self.data[((k % m) + (1 + (k % m-1)) * i) % m] = (k,v)
                    return
                elif self.data[((k % m) + (1 + (k % m-1)) * i) % m][1] == "DEL":
                    self.data[((k % m) + (1 + (k % m-1)) * i) % m] = (k,v)
                    return
                else:
                    i += 1
            
        return

    def remove(self, k):
        ##
        assert int == type(k) and k >= 0
        i = 0
        m = self.tablesize
        if k == self.data[((k % m) + (1 + (k % m-1)) * i) % m][0]:
            self.data[((k % m) + (1 + (k % m-1)) * i) % m] = (k, "DEL")
        else:
            for j in self.data:
                if self.data[((k % m) + (1 + (k % m-1)) * i) % m][0] == k:
                    self.data[((k % m) + (1 + (k % m-1)) * i) % m] = (k, "DEL")
                    return
                else:
                    i += 1             
        return 

    def get(self, k):
        assert int == type(k) and k >= 0
        i = 0
        m = self.tablesize
        if self.data[((k % m) + (1 + (k % m-1)) * i) % m][0] == k:
            return self.data[((k % m) + (1 + (k % m-1)) * i) % m][1]
        elif self.data[((k % m) + (1 + (k % m-1)) * i) % m][0] != k:
            for j in self.data:
                if self.data[((k % m) + (1 + (k % m-1)) * i) % m][0] == k:
                    return self.data[((k % m) + (1 + (k % m-1)) * i) % m][1]
                else:
                    i += 1

        return

class FootableQuadratic(Footable):
    def __init__(self):
        return Footable.__init(self)

    
    def put(self, k, v):
        assert int == type(k) and k >= 0
        i = 0
        c1 = 0.5
        c2 = 0.5
        m = self.tablesize
        if None == self.data[((k % m) + c1*i + c2*i*i) % m]:
            self.data[((k % m) + c1*i + c2*i*i) % m] = (k,v)
        elif "DEL" == self.data[((k % m) + c1*i + c2*i*i) % m][1]:
            self.data[((k % m) + c1*i + c2*i*i) % m] = (k,v)
        else:
            ## keep probing till empty space is found
            for j in self.data:
                if self.data[((k % m) + c1*i + c2*i*i) % m] == None:
                    self.data[((k % m) + c1*i + c2*i*i) % m] = (k,v)
                    return
                elif self.data[((k % m) + c1*i + c2*i*i) % m][1] == "DEL":
                    self.data[((k % m) + c1*i + c2*i*i) % m] = (k,v)
                    return
                else:
                    i += 1
            
        return

    def remove(self, k):
        ##
        assert int == type(k) and k >= 0
        i = 0
        c1 = 0.5
        c2 = 0.5
        m = self.tablesize
        if k == self.data[((k % m) + c1*i + c2*i*i) % m][0]:
            self.data[((k % m) + c1*i + c2*i*i) % m] = (k, "DEL")
        else:
            for j in self.data:
                if self.data[((k % m) + c1*i + c2*i*i) % m][0] == k:
                    self.data[((k % m) + c1*i + c2*i*i) % m] = (k, "DEL")
                    return
                else:
                    i += 1             
        return 

    def get(self, k):
        assert int == type(k) and k >= 0
        i = 0
        c1 = 0.5
        c2 = 0.5
        m = self.tablesize
        if self.data[((k % m) + c1*i + c2*i*i) % m][0] == k:
            return self.data[((k % m) + c1*i + c2*i*i) % m]
        elif self.data[((k % m) + c1*i + c2*i*i) % m][0] != k:
            for j in self.data:
                if self.data[((k % m) + c1*i + c2*i*i) % m][0] == k:
                    return self.data[((k % m) + c1*i + c2*i*i) % m]
                else:
                    i += 1

        return
    
        

    

    

        

    
