#!/usr/bin/env python

import sys
import random

# Arguments: fn is the function to be evaluated; size is the size of
# the keyspace; vals is the set of values to use for evaluation.
# Returns a tuple: 0) load factor (proportion of values stored to
# number of slots) 1) proportion of nonempty slots 2) number of values
# that collide with another value 3) mean size of nonempty slot (as a
# float) 4) median size of nonempty slot (as a float) 5) size of
# largest slot
def hashEval(fn, size, vals):
  #load factor
  results = []
  load_factor = float(len(vals)) / size
  results.append(load_factor)

  #proportion of nonempty slots
  #number of values that collide with another value
  
  hashs = [None] * size
  slots = []
  slotsizes = [0]
  collisions = 0
  
  for v in vals:
    if hashs[fn(v)] == None:
      hashs[fn(v)] = [v]
      slots.append(fn(v))
    else:
      hashs[fn(v)].append(v)
      collisions += 1
      
  proportion = len(slots) / float(size)
  results.append(proportion)
  results.append(collisions)

  # mean size of nonempty slot
  meanslotsize = len(vals) / float (len(slots))
  results.append(meanslotsize)

  #median size of nonempty slot
  for s in hashs:
    if s != None:
      slotsizes.append(len(s))
    
  slotsizes.sort()
  medslotsize = slotsizes[len(slotsizes)/2]
  results.append(medslotsize)

  #largest slot size
  maxslotsize = max(slotsizes)
  results.append(maxslotsize)

  return results
      
  
  


# Returns an iterable collection of qty random ints less than size.
# The ints should be uniformly distributed.
def randInts(size, qty):
  iter1 = []
  for e in range(qty):
    iter1.append(int(random.uniform(0, size)))
  print iter1
  return iter1
    

# Who says we aren't nice to you?  A simple helper function that
# pretty-prints the results of hashEval().
def printHashEval(fn, size, vals):
  result = hashEval(fn, size, vals)
  print "Load factor:\t\t" + str(result[0])
  print "Proportion nonempty:\t" + str(result[1])
  print "Collisions:\t\t" + str(result[2])
  print "Mean size:\t\t" + str(result[3])
  print "Median size:\t\t" + str(result[4])
  print "Max size:\t\t" + str(result[5])

# Takes a list of ints x representing a set and returns an integer
# hash.
def setHash(vals):
  BASE = 37
  x = 1
  for v in vals:
    x = (x * BASE) + v
  return x % sys.maxint

printHashEval(lambda x: x, 8, randInts(6, 8))



#Takes the sum of the list of ints v in vals mod the
#Collisions may be resolved by chaining
def newSetHash(vals):
  BASE = 37
  x = 1
  vals = vals.sort()
  for v in vals:
    x = (x * BASE) + v
  return x % sys.maxint
