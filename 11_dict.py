d = {}  # empty dictionary
marks = {
    "Aashi":100,
    "Surbhi":89,
    "Rohan":23
}
print(marks,type(marks))
print(marks["Surbhi"])

# properties of python dictionaries
# 1.  it is unordered
# 2.  it is mutable 
# 3.  it is indexed
# 4.  cannot contain duplicate keys.

# dict_method
print(marks.items())
print(marks.keys())
marks.update({"Aashi":99})
marks.update({"Nitya":100})
marks.update({"Rohan":70,"Raunak":59})
print(marks)
print(marks.get("Shivika"))
print(marks.get("Aashi"))
print(marks.get("Aashi"))
print(marks.get("Aashi2")) # give output none
print(marks["Aashi2"]) # give error

# Dictionary Methods in Python:
# dict.clear() – Removes all items from the dictionary.

# dict.copy() – Returns a shallow copy of the dictionary.

# dict.fromkeys(iterable, value) – Creates a new dictionary from an iterable with specified values.

# dict.get(key, default) – Returns the value for the given key, or the default value if the key is not found.

# dict.items() – Returns a view object of dictionary’s key-value pairs.

# dict.keys() – Returns a view object of dictionary keys.

# dict.values() – Returns a view object of dictionary values.

## dict.pop(key, default) – Removes the key and returns its value, or the default if the key is not found.

## dict.popitem() – Removes and returns the last inserted key-value pair.

# dict.setdefault(key, default) – Returns the value of the key if it exists; otherwise, sets it to the default value.

# dict.update(other_dict) – Updates the dictionary with key-value pairs from another dictionary or iterable.

# dict.__contains__(key) – Checks if the key exists (key in dict is preferred).

# dict.__len__() – Returns the number of items in the dictionary (len(dict) is preferred).

# dict.__delitem__(key) – Deletes the item with the given key (del dict[key] is preferred).








