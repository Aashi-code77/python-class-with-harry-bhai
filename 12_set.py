s = set() # dont use s = {} as it will create an empty dictionary 
#  always use s = set() -- this is empty set 
print(type(s))  # <class 'set'>
s= {1,5,32,54,5,5,5} # unordered 

print(s)

# set_method
s= {1,5,32,54,5.78,"Aashi",5}  
print(s,type(s))
s.add(577)
print(s,type(s))

# SOME IMPORTANT METHOD OF SET

# set.add(element) – Adds an element to the set.

# set.remove(element) – Removes an element; raises an error if the element is not found.

# set.discard(element) – Removes an element if it exists; does nothing if it doesn’t.

# set.pop() – Removes and returns a random element from the set.

# set.clear() – Removes all elements from the set.

# set.union(set2) or set | set2 – Returns a new set containing elements from both sets.

# set.intersection(set2) or set & set2 – Returns a new set with common elements.

# set.difference(set2) or set - set2 – Returns elements that are only in the first set.

# set.symmetric_difference(set2) or set ^ set2 – Returns elements in either set, but not both.

# set.issubset(set2) or set <= set2 – Checks if the set is a subset of another.

# set.issuperset(set2) or set >= set2 – Checks if the set is a superset of another.

# set.isdisjoint(set2) – Returns True if both sets have no elements in common.

# set.update(set2) or set |= set2 – Adds elements from another set to the current set.

# set.intersection_update(set2) – Keeps only elements found in both sets.

# set.difference_update(set2) – Removes elements found in another set.

#  properties of sets 
# 1. Sets are unordered => Element's order doesn't matter 
# 2. Sets are unindexed => Cannot access elements by index
# 3. there is no way to change items in sets.
# 4. Sets cannot contain duplicate values.



# Operations on sets

# 1. Adding & Removing Elements

# set.add(element): Adds an element to the set.

# set.remove(element): Removes an element; raises an error if not found.

# set.discard(element): Removes an element if it exists, without error.

# set.pop(): Removes and returns a random element.

# set.clear(): Removes all elements.

# len(set) : the length of the set.

# 2. Set Union (Combining Sets)

# set1 | set2 or set1.union(set2): Combines elements from both sets.


# 3. Set Intersection (Common Elements)

# set1 & set2 or set1.intersection(set2): Returns only elements found in both sets.


# 4. Set Difference (Unique Elements)

# set1 - set2 or set1.difference(set2): Returns elements only in set1.


# 5. Symmetric Difference (Exclusive Elements)

# set1 ^ set2 or set1.symmetric_difference(set2): Returns elements in either set, but not both.


# 6. Checking Subsets and Supersets

# set1.issubset(set2) or set1 <= set2: Checks if set1 is a subset of set2.

# set1.issuperset(set2) or set1 >= set2: Checks if set1 is a superset of set2.


# 7. Checking Disjoint Sets

# set1.isdisjoint(set2): Returns True if sets have no elements in common.


# 8. Updating Sets

# set1.update(set2): Adds elements from set2 to set1.

# set1.intersection_update(set2): Keeps only common elements.

# set1.difference_update(set2): Removes elements found in set2.













