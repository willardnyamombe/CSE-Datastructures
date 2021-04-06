# **SETS**
## **INTRODUCTION**
A set is a data structure that allows multiple items to be stored in a single variable. It allows the storage of multiple data like integers, floats, and strings etc. Sets do not worry about **order or index** when storing data. One thing to remember is that sets can store **unique** values and doesn't add **duplicates**.
When creating a set we use **curly** brackets for example:
```python
my_set = {1,'apple',10.2,'apple'}
print(my_set)

{1, 10.2, 'apple'}#this is the result after the print statement
```
As you might have noticed our set here is storing multiple data. And the order is different now from what we saw when the set was created. Do not panic!! This is perfectly normal because sets change their order automatically almost always.  
Did you notice something else?  
I bet you did! Initially there were 2 apples in the set but we only saw one in the result set.   
What might have happened?   
You guessed it!! Sets dont allow **duplicates**.

## **ATTRIBUTES OF A SET AND SET OPERATIONS**
The main operations we will talk about are the add, remove, size and how to access an item in a set.
## *Add Function*
First lets create a variable that will take the empty set and we call it myset: `myset = set()`   
In order to add items in  `myset` we use the `myset.add()`. Inside the bracket we can pass in a single argument.    
Lets look at the code below:
```python
myset = set()
myset.add('mango')
myset.add("apple")
myset.add(1)
#result
{'mango', 1, 'apple'} 
 ```
## *Remove Function*
To remove an item inside `myset` we use `myset.remove()`. Inside the bracket we can pass in a single argument.
Sets also allow the use of a `pop()` function which only removes the last item in a set. And the pop fuction does not take any arguments.
Check out the example code below:
```python
myset = {'mango', 1, 'apple'}
myset.remove('mango')
#result
{1, 'apple'}
```
## *Size or length(len) Function*
It is sometimes wise when working with data to know the size or length of the data we are working with.
The length or `len` function does allow us to get the size of a set. 
**#** (This also works for other data types like lists and tuples)    
In order to find the length of `myset` we use `len(myset)`.
See the code snippet below on how the length function can be used.
```python
myset = {'mango', 1, 'apple'}
print(len(myset))
#result
3
```
## **Problem!**
Here is a simple problem for you to work out.      
All you need to do here is to create a new set and call it bag3. Then find the union and the intersection for the 2 sets without using a python built-in union and intersection.
```python
bag1 = {'phone','cash','book','earphones'}
bag2 = {'mango','cash','banana','book'}
#create and empty set and call it bag3
 enter code here
#Then find the union
 enter code here
The result for this union should print: Union = {'banana', 'cash', 'phone', 'earphones', 'book', 'mango'}
# Now comment out your union code and then solve for the intersection
enter you code here
The result for this intersection should print: Intersection = {'book', 'cash'}
```
If you get stuck here is the [solution ](https://github.com/willardnyamombe/CSE-Datastructures/blob/main/DatastructureTutorials/setssolution.md) to this problem.   

 
 
 
