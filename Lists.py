# Python Assignment 4

"""course:Python,assigment:homework#4
How the program works;
the function add item to the myUnique list input by the user and returns the list.
if the item is already in the list

the item is not added instead the use is informed and prompted to enter another item
while there is still room in the list;item_size defines how many items the user should input
Alternatively if the items is in the list,it is not added the list.

my problem/query;
 how to make the function return True if item is not in the myUniqueList
or False if the item is not.Having True/False in the if statement seems to terminates the loop """

myUniqueList = []


def addToList(items_size):
    global myUniqueList
    for n in range(items_size):  # prompting the user for input as many as the number of items
        item = input("enter number :")
        if item not in myUniqueList:
            myUniqueList.append(item)
            print(True)# return True
        else:
            print(False)

    return myUniqueList


numberOfItem = 5  # sample data: 1,2,a,a,f
print(addToList(numberOfItem))

# adding more items to the same list checking is item is on the list
numberOfItem = 4  # sample data: 5,2,8,f
print(addToList(numberOfItem))
