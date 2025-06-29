#1-> Write a Python program to add elements to a list using insert() and append(). 

fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits.append("date")
print(fruits)

fruits.insert(1, "blueberry") 
print(fruits)

 
fruits.insert(0, "kiwi")
print(fruits)


#2-> Write a Python program to remove elements from a list using pop() and remove().


fruits = ["apple", "banana", "cherry", "date", "banana"]
print(fruits)


fruits.pop(2)  
print(fruits)


fruits.pop()
print(fruits)

fruits.remove("banana")
print(fruits)