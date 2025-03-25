guru = 'Harry'
print(type(guru))
me = " Aashi"
print(type(me))
sister = '''Nitya'''
print(type(sister))
#  string is immutable and string is a data type in python .
# string is a sequence of character enclosed in quotes.
#  we can primarly write a string in three way (('') - single quoted string ,(" ") - double quoted string ,(''' ''') - triple quoted string ).

#  A string in python can be sliced for getting a part of the strings.
#  harry -- length = 5 and jb hm sidha count krte h to 0 se start krte h like  ( h (0),a (1),r(2),r(3),y(4)) but ulta count me -1 se start krte h  (y (-1),r(-2),r(-3),a(-4),h(-5))
name = "Aashi"
nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)  # it also count space
character1 = name[1]
print(character1)
print(name[-4:-1])
print(name[:4]) # is same as print(name[0:4])
print(name[1:]) #is same as print(name[1:5])
print(name[1:5])

# Slicing with skip value
a = "123456789"
print(a[1:7:3])
b = "abcdefghijklmnopqrstuvwxyz"
print(b[1:9:4])
print(b[1:9])
