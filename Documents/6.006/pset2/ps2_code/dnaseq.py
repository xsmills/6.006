#!/usr/bin/env python2.7

import unittest
#from dnaseqlib import *

### Utility classes ###

# Produces hash values for a rolling sequence.
class RollingHash:
    # Initializes a new rolling hash of the iterable sequence s.
    # (Remember that, in Python, this includes strings!)
    def __init__(self, s):
        self.string = s
        self.hash_val = 0
        self.base = 8
        for i in range(len(self.string)):
            self.hash_val += ord(self.string[i]) * (self.base**(len(self.string) - 1 - i))

    # Returns the current hash value.
    def hash(self):
        
        return self.hash_val
            

    # Updates the hash by removing previtm and adding nextitm.
    # Returns the updated hash value.
    def slide(self, previtm, nextitm):
        new_hash_val = self.base*(self.hash_val - ((self.base**(len(self.string) - 1)) * ord(self.string[0]))) + ord(nextitm)
        self.hash_val = new_hash_val
        self.string = self.string[1:] + nextitm
        return new_hash_val
        

# Maps integer keys to a set of arbitrary values.
class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        self.dict = {}
        for (k,v) in pairs:
            self.dict[k] = [v]
            
    # Associates the value v with the key k.
    def put(self, k, v):
        if k not in self.dict:
            self.dict[k] = [v]
        else:
            self.dict[k].append(v)
    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):
        if k not in self.dict:
            return []
        else:
            return self.dict[k]

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)
def subsequenceHashes(seq, k):
    a = ""
    i = 0
    lastSubseq = False
    try:
        for e in range(k):
            a += seq.next()
            print a
            i += 1
        
        hash_a = RollingHash(a).hash()

        hash_a = RollingHash(a).slide(a[0], seq.next()[-1])
        yield (a, hash_a, lastSubseq)

        


    except StopIteration:
        lastSubseq = True

        
        
        
# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):
    raise Exception("Not implemented!")

# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k, m):
    table = Multidict()
    
    seq_a = subsequenceHashes(a, k)
    seq_b = subsequenceHashes(b, k)

    matches = []

    return matches


# Uncomment this when you're ready to generate comparison images.  The
# arguments are, in order: 1) Your getExactSubmatches function, 2) the
# filename to which the image should be written, 3) a tuple giving the
# width and height of the image, 4) the filename of sequence A, 5) the
# filename of sequence B, 6) k, the subsequence size, and 7) m, the
# sampling interval for sequence A.
#compareSequences(getExactSubmatches, 'maternal-paternal.png', (500,500), 'fmaternal.fa', 'fpaternal.fa', 20, 10000)

### Testing ###

class TestRollingHash(unittest.TestCase):
    def test_rolling(self):
        rh1 = RollingHash('abcde')
        rh2 = RollingHash('bcdef')
        rh3 = RollingHash('cdefZ')
        rh1.slide('a','f')
        print rh2.hash()
        print rh1.hash()
        self.assertTrue(rh1.hash() == rh2.hash())
        rh1.slide('b','Z')
        self.assertTrue(rh1.hash() == rh3.hash())

class TestMultidict(unittest.TestCase):
    def test_multi(self):
        foo = Multidict()
        foo.put(1, 'a')
        foo.put(2, 'b')
        foo.put(1, 'c')
        self.assertTrue(foo.get(1) == ['a','c'])
        self.assertTrue(foo.get(2) == ['b'])
        self.assertTrue(foo.get(3) == [])

# This test case may be useful before you add the argument m
#class TestExactSubmatches(unittest.TestCase):
#    def test_one(self):
#        foo = 'yabcabcabcz'
#        bar = 'xxabcxxxx'
#        matches = list(getExactSubmatches(iter(foo), iter(bar), 3, 1))
#        correct = [(1,2), (4,2), (7,2)]
#        self.assertTrue(len(matches) == len(correct))
#        for x in correct:
#            self.assertTrue(x in matches)

if __name__ == '__main__':
   unittest.main()
