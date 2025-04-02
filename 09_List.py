# LIST 
a = [4,6,7]
print(type(a)) # <class 'list'>
friends = ["Apple","orange",5,345.06,False,"Aakash", "Rohan"]
print(friends[0])
friends[0] = "Grapes" # ab apple ke place pr grapes show hoga 
print(friends[0]) # we know ki string  are immutable but list are mutable , index are start with 0 just like in string 
print(friends[1:4])

# LIST_METHODS
friends.append("Aashi") # append -- friends ke list me last me Aashi jor deta h to ab 7 ke jagah pr 8 chizo ka list h 
print(friends)

l1 =[1,334,62,2,6,11]
# l1.sort() # it arrange the number in assending order by default
# l1.reverse()
# l1.insert(3,3333) # at index = 3 in that place it insert 3333 ( index,object)
value=l1.pop(2) # pop -- dlt ( here pop dlt the object jaha index = 2  hai .)  
#  here value ek variable h 
print(value)
l1.remove(2)  # here remove dlt the object jaha index = 2
print(l1)
