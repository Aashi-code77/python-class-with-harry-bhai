# TUPLE
a = (2,7,9,0)
print(a)
print(type(a)) #<class 'tuple'>
a=(1) # # <class 'int'>
print(type(a))
a=(1,) # <class 'tuple'>
print(type(a))


# TUPLE_METHODS
a = ( 67,8.90,True,"rohan", 67,'yamini')
print(a)
no = a.count(67)
print(no)
i = a.index(67)
print(i)
repeated = a*3
print(repeated)
print(8.9 in a) # True
sliced = a[1:4]
print(sliced)
unpacking = (1,2,3)
a,b,c = unpacking
print(a,b,c) # output : 1 2 3



# 1.Convert Tuple to List (Modify Indirectly)
# You can convert a tuple into a list, modify it, and then convert it back into a tuple.
my_tuple = (1, 2, 3)
temp_list = list(my_tuple)  # Convert to list
temp_list.append(4)  # Modify the list
my_tuple = tuple(temp_list)  # Convert back to tuple
print(my_tuple)  # Output: (1, 2, 3, 4)


# 2. Concatenation (Creating a New Tuple)
# You can create a new tuple by concatenating existing tuples.
t1 = (1, 2, 3)
t2 = (4, 5)
new_tuple = t1 + t2
print(new_tuple)  # Output: (1, 2, 3, 4, 5)


# 3. Slicing (Extracting a Subset)
# You can extract a portion of a tuple using slicing.
my_tuple = (10, 20, 30, 40, 50)
new_tuple = my_tuple[1:4]  # Extracts elements from index 1 to 3
print(new_tuple)  # Output: (20, 30, 40)


# 4. Reassignment (Replacing Entire Tuple)
# Since tuples are immutable, you cannot change individual elements, but you can reassign a new tuple to the same variable.
my_tuple = (1, 2, 3)
my_tuple = (4, 5, 6)  # Reassigning a new tuple
print(my_tuple)  # Output: (4, 5, 6)


# 5. Nesting (Tuples Inside Tuples)
# Although you cannot change a tuple itself, you can modify a mutable object inside a tuple, like a list.
my_tuple = (1, [2, 3], 4)
my_tuple[1].append(5)  # Modifying the list inside the tuple
print(my_tuple)  # Output: (1, [2, 3, 5], 4)


# What You CANNOT Do in Tuples:
# ❌ No element reassignment → tup[0] = 10 will cause an error.
# ❌ No direct element addition/removal → append(), insert(), and remove() are not available.