LIST NOTES - from W3Schools.com/python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# 1. Accessing list items
print(thislist[1]) # print the second item of the list
print(thislist[-1]) # print the last item of the list
print(thislist[2:5]) # return the third, fourth, and fifth item
print(thislist[:4]) # returns the items from the beginning to, but NOT including,
"kiwi"
print(thislist[2:]) # returns the items from "cherry" to the end
print(thislist[-4:-1]) # returns the items from "orange" (-4) to, but NOT including
"mango" (-1)
# check if "apple" is present in the list
if "apple" in thislist:
 print("Yes, 'apple' is in the fruits list")
# 2. Changing list items
thislist[1] = "blackcurrant" # Change Item Value
thislist[1:3] = ["blackcurrant", "watermelon"] # Change a Range of Item Values
thislist[1:3] = ["watermelon"] # change the second and third value by replacing it
with _one_ value
thislist.insert(2, "watermelon") # insert "watermelon" as the third item
# 3. Adding list items
thislist.append("orange") # append() method appends/adds an item
thislist.insert(1, "orange") # insert() method inserts an item at the specified
index/here insertes "orange" in second posiion
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # add the elements of `tropical` to `thislist`
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) # add elements of a tuple to a list
# 4. Removing list items
thislist.remove("banana") # remove the first occurrence of "banana" if it is
occured many times
thislist.pop(1) # Remove Specified Index/remove the second item
thislist.pop() # If not specified the index, pop() removes the laste item
del thislist[0] # del keyword also removes the specified index/here the first item
del thislist # delete the entire list
thislist.clear() # clear the list content
# 5. Loop lists
# print all items in the list, one by one
for x in thislist:
 print(x)
# print all items by referring to their index number
for i in range(len(thislist)):
 print(thislist[i])
# print all items, using a `while` loop to go through all the index numbers
i = 0
while i < len(thislist):
 print(thislist[i])
 i = i + 1
# looping Using List Comprehension
# a short hand `for` loop that will print all items in a list
[print(x) for x in thislist]
# 6. List comprehension
# Without list comprehension
newlist = []
for x in thislist:
 if "a" in x:
 newlist.append(x)
# With list comprehension you can do all that with only one line of code:
newlist = [x for x in thislist if "a" in x]
# Syntax: newlist = [expression for item in iterable if condition == True]
newlist = [x for x in thislist if x != "apple"] # Only accept items that are not
"apple":
newlist = [x for x in thislist] # with no `if` statement
newlist = [x for x in range(10)] # you can use the `range()` function to create an
ITERABLE
newlist = [x for x in range(10) if x < 5] # Same example, but with a condition || #
accept only numbers lower than 5
# Expression
newlist = [x.upper() for x in thislist] # set the values in the new list to upper
case
newlist = ['hello' for x in thislist] # set all values in the new list to 'hello'
newlist = [x if x != "banana" else "orange" for x in thislist] # return "orange"
instead of "banana"
# 7. Sorting
thislist.sort() # sort the list alphabetically/in ascending order
thislist.sort(reverse = True) # sort the list in descending order
thislist.sort(key = str.lower) # Performs a case-insensitive sort of the list
thislist.reverse() # Reverse the order of the list items:
# sort the list based on how close the number is to 50
def myfunc(n):
 return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# 8. Copying Lists
# You cannot copy a list simply by typing list2 = list1, because: list2 will only
be a reference to list1, and changes made in list1 will automatically also be made
in list2.
mylist = thislist.copy()
mylist = list(thislist) # Another way to make a copy is to use the built-in method
list().
mylist = thislist[:] # You can also make a copy of a list by using the : (slice)
operator.
# 9. Joining Lists
list3 = list1 + list2 # Joins two lists
# Appending list2 into list1:
for x in list2:
 list1.append(x)

# Or you can use the extend() method, where the purpose is to add elements from one
list to another list:
# Use the extend() method to add list2 at the end of list1:
list1.extend(list2)
"""
Method Description
append() Adds an element at the end of the list
clear() Removes all the elements from the list
copy() Returns a copy of the list
count() Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current
list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list
"""