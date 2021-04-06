# **Stack**
## **INTRODUCTION**
A stack is a data structure that allows items to be added and removed. The other truth about a stack data structure is that items within it are not accessed randomly. You can not access an object at the front and or the middle of a stack. The only option available is that you can access the last item that was added first and in that order, hence the famous name for this type of data structure is known as **LIFO**(Last In First Out).

## **Push and Pop Operations**
These two operations are only implemented from the back of the stack. For example, if we want to add or remove `3` to a stack with a variable name of `numbers` that has 2 objects or items in it in the form of `1` and `2`, we get the following results:

```python
numbers = [1,2] #before adding 3

numbers = [1,2,3] #after adding 3

numbers = [1,2] #After removing 3
 ```

 ## **Push**
 The adding operation is what is called the **Push** operation. This can only add the new value to the end or the back of a stack.
 
  **#** This is the only way to add an object in the stack data structure.

In order to implement the **Push** operation we use the python built-in ***append()*** function. We are also required to specify the item we want to append or add to the stack. If we want to append `3` we start by mentioning the name of the stack and then using a dot(.) notation we link the append statement and add the item inside the brackets as follows: `name_of_stack.append(3)`.  
Here is a simple python ***EXAMPLE*** of how `3`, `4`, and `0` are appended to `numbers` which already has `[1,2]` in it.

```python
numbers = [1,2] #initial values before adding anything

def push(num): #this function is adding or appending a value to the stack called numbers
    return numbers.append(num)

def check(): # this function is checking the content inside the stack called numbers
        print(numbers)

#Tests
# Pushing into stack a new value, then checking to see the added values.
print()
print("===Whats in Numbers?===") 
check()
print("=====Test 1======")# add i item
push(3)
check()
print("=====Test 2======")#Add 2 more items
push(4)
push(0)
check()
```
The perfomance of this operation is **O(1)**.


## **Pop**
The remove operation from the example above is what is called the **Pop** operation. 

**#** This removes the last item that was added.  

  In order to implement the **Pop** operation we use the python built-in **pop()** function.

 Let me give an ***EXAMPLE***:
```python

numbers = [1,2,3] #
numbers.pop() # removing last items added to the stack
print(numbers)

#the result after running the print statement will be:
[1,2]


```


## **Perfomance**
What is **O(1)**? This comes from the term **Big O Notation**.   
The Big O notation is what computer scientist use to calculate the perfomance of an algorithm when the size of the details is large. Depending on the size of the data we will be able to know how much time it will take to complete the function.  The Push and/or Pop operation for the above code examples is ***constant time*** or one unit of time because the value goes to a specified location. 

## **Real world uses of a Stack data structure**
We use the **pop** function when we click the back button on a browser. The pop function or back button will return to the last page that was visited.  
The **push** function is when we search for a webpage and then as soon as we are on the webpage that means we have just added that page to our stack. This website will be at the back of the stack now.  
Assuming you are familiar with classes in python here is a ***PROBLEM*** for you to solve:
```python
""" 
    **First part**
    >Create a class and name it browser
     >Using the init method initialize 2 attributes named website and page_visited
     >Then set website as an empty array
     >Set page_visited to None
     >You can copy the code below:
    """
class browser:
    def __init__(self):
        self.website = []
        self.page_visited = None
"""
    **Second part**
    >create a push function that will add a name of a visited webpage to the empty website list
"""
# type your code here

"""
    **Third part**
    >create a pop function that will remove a name of a last visited webpage from the website list
"""
    # type your code here
"""
    **Third part**
    finish writing the code for the function below. This function should display the names of webpages that that are inside the website list.
"""
    def check(self):
    # type your code here

"""
    **Last part**
    Complete test cases below
"""
browser = browser()
#Test 1 is adding the first webpage to the website list 
print("========Test One========")
add "www.byui.edu"
print()
print(browser.check())
print()
#Test 2 is adding the 2nd web page to the website list
print("========Test Two========")
print()
add "www.facebook.com"
print(browser.check())
print()
#Test 3 is adding the 3rd web page to the website list
print("========Test Three========")
add "www.instagram.com"
print(browser.check())
print()
#Test 4 is removing the last web page visited from the website list
print("========Test Four========")
print(browser.check())
print()

```
In the problem above we will use ***test cases*** to make sure that it is clear how items are being added to the stack as well as how there are removed. We should be able to see the ***Pop*** and ***Push*** functions in actions. And for you to be able to see what was happening inside the stack we created a ***check*** function for that.  
If you get stuck here is the [solution ](https://github.com/willardnyamombe/CSE-Datastructures/blob/main/stacksolution.md) to this problem.
