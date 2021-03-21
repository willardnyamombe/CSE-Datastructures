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
Here is a simple python example of how `3` was added or appended to `numbers`.

```python
numbers = [1,2] #initial values of numbers
numbers.append(3) # adding 3 to the stack
print(numbers)

#the result after running the print statement will be:
[1,2,3]
```
The perfomance of this operation is **O(1)**.


## **Pop**
The remove operation from the example above is what is called the **Pop** operation. 

**#** This removes the last item that was added.  

  In order to implement the **Pop** operation we use the python built-in **pop()** function.

 Let me give an example:
```python

numbers = [1,2,3] #
numbers.pop() # removing last items added to the stack
print(numbers)

#the result after running the print statement will be:
[1,2]


```


# PERFORMANCE
What is **O(1)**? This comes from the term **Big O Notation**.   
The Big O notation is what computer scientist use to calculate the perfomance of an algorithm when the size of the details is large. Depending on the size of the data we will be able to know how much time it will take to complete the function.  The Push and/or Pop operation for the above code examples is ***constant time*** or one unit of time because the value goes to a specified location. 