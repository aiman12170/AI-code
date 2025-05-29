# question 1
x = "5"
y=10
# print(x+y) # error
z=int(x) #x is now int
print(y+z)     

a = 3.14
print(type(a))   # Output: <class 'float'>


# question 2
#Access items
fruits = ["apple", "banana", "cherry","Apple","Cherry","Watermelon"]
print(f"the element at index 1 is: {fruits[1]}")
#Use loops
for fruit in fruits:
    print(fruit)
#Add items:
fruits.append("orange")
fruits.insert(1, "mango")
print(f"List after insertion: {fruits}")
#Remove items
fruits.remove("banana")
fruits.pop(0)
print(f"List after remove: {fruits}")
#Sort list
fruits.sort()     # Ascending
fruits.sort(reverse=True)  # Descending
#Copy list:
new_list = fruits.copy()
print(f"List after copy: {fruits}")
cube=[i**3 for i in range(1,11) if i%2==0] #list comprehension
print(cube)



# Question 3
t = ("apple", "banana", "cherry")
t1 = ("apple", "mango", "orange")

print(f"Element at index 1 is: {t[1]}")  
for item in t:
    print(item)
# updating a tuple(indirectly)
temp = list(t)
temp.append("Orange")
t = tuple(temp)
print(f"tuple after updating: {t}")
# unpacking a tuple:
print("Unpacking tuple")
a, b, c, d = t
print(a)  
print(b)
print(c)
print(d)
# Joining tuples:
print("Joining two tuples: ")
join=t+t1
print(join)
# tuple methods
print("tuple methhod: ")
print(join.count("apple"))


# question 4
s={1,2,3,4,5,6}
s1={10,11,23,45,78,9}
s2={10,23,55,67,11}
print(f"Original set: {s}")
s.add(8)
print(f"After adding element: {s}")
s.remove(4)
print(f"After removing element: {s}")
s.pop()
print(f"After poping random element: {s}")
s.discard(10)
print(f"After discard element not in set: {s}")
s.clear()
print(f"After clearing set: {s}")
union=s1.union(s2)
print(f"Union of Two sets: {union}")
intersection=s1.intersection(s2)
print(f"Intersection of Two sets: {intersection}")


# question 5
import array
print("Array")
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)
print("Basic operations")
arr.append(6)
print(arr)

import numpy as np
print("NumPy array")
arr = np.array([1, 2, 3, 4, 5])
print(arr) 
print("Basic operations")
print(f"Addition: {arr + 2}")  
print(f"subtraction: {arr - 2}") 


# question 6
print("Initial list")
shopping_list = ["milk","bread","eggs","butter","juice","sugar","salt","biscuits","tea","coffee"]
for items in shopping_list:
    print(items)
add_item=input("Do you want to add new item..") 
if add_item.lower()=="yes":  
    new_item=input("Enter new item: ")
    shopping_list.append(new_item)   
    print(new_item, "is added in the list")
remove_item=input("Do you want to remove item (yes/no)")
if remove_item.lower=="yes":
    item_to_remove=input("Enter item to remove: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
    else:
        print("Item not found")   
print("Updated list")
for items in shopping_list:
    print(items)


# question 7
num=int(input("Enter a number: "))
def check_even_odd(num):
    if num%2==0:
        print(num, "is even number")
    else:
        print(num, "is odd number ")
check_even_odd(num)

def cal_sum(a=2,b=2):
      c=a+b
      print(c)
      return c
cal_sum()

def sub(a,b):
    S=a-b
    return S
print(sub(2,5))


# question 8
import random
random_number=random.randint(1,100)
print(f"Random number generated is {random_number}") #generate a random number between 1 to 100


# question 9
student_marks=(90,67,45,12,57,87) # tuple
#print first and last number of tuple 
print("First element of tuple is ", student_marks[0])
print("Last element of tuple is ", student_marks[-1])
#unpacking tuple 
print("Unpacked tuple ")
m1,m2,m3,m4,m5,m6=student_marks
print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print(m6)
new_tuple=list(student_marks)
for i in range(len(new_tuple)):
    new_tuple[i]+=5
new_tuple=tuple(new_tuple)
print("Original tuple")
print(student_marks)
print("New tuple")
print(new_tuple)


# question 10
numbers = [5, 12, 7, 18, 9, 24, 3, 16, 11]
divisible_by_3 = 0
even_not_divisible = 0
odd_not_divisible = 0
for num in numbers:
    if num % 3 == 0:
        print(num," is divisible by 3")
        divisible_by_3 += 1
    elif num % 2 == 0:
        print(num," is even but not divisible by 3")
        even_not_divisible += 1
    else:
        print(num," is odd and not divisible by 3")
        odd_not_divisible += 1
print("Numbers divisible by 3: ", divisible_by_3)
print("Numbers even but not divisible by 3: ", even_not_divisible)
print("Numbers odd and not divisible by 3: ", odd_not_divisible)


# question 11
def classify_numbers(numbers):
    counts = {"positive": 0, 
              "zero": 0, 
              "negative": 0}
    for num in numbers:
        if num > 0:
            print(num, " is positive")
            counts["positive"] += 1
        elif num == 0:
            print(num," is zero")
            counts["zero"] += 1
        else:
            print(num," is negative")
            counts["negative"] += 1
    return counts
numbers = [50, -93, 0, -22, -14, 0, 49, -29]
result = classify_numbers(numbers)
print("Counts:")
print("Positive: ", result['positive'])
print(f"Zero: {result['zero']}")
print(f"Negative: ",result['negative'])



 












