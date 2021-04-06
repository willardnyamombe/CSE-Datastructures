# **TREES**
## **INTRODUCTION**
A Tree data structure looks like a tree as its connects nodes and theres is a way to go from the root nodes to every other node whether left or right side. There cant be 2 references or pointers pointing to one node.     
There are different types of trees but I will talk about Binary trees and Binary Search Trees(BST).

## **Binary trees**
These trees have a top most node which is called a `Root node` and theres only one root node per tree. This is generally the starting point. Consider looking at a tree upside down. The roots up as the first node , branches going down left to right as left and right nodes. If a node doesnt connect to any other node it is called a `leaf node`. A `parent node` is one that has connected node. these nodes that are connected to the parent node are called `child nodes`. The left and right nodes that are connected to the parent node form a ` subtree`. See figure below:   

![Concept Diagram for Binary tree](https://www.guru99.com/images/1/020820_0600_BinarySearc1.png)     
(obtained from www.guru99.com)
## **Binary Search Tree(BST)**
This is a special type of binary tree where the element or data in the nodes have a specific order. All nodes on the left side of the parent nodes are less than the value of the parent node. And on the right side on the parent node we will see values higher than the values in the parent node. The other property for this tree is that data or values in nodes are unique. It doesnt take duplicates.    
*This type of data helps to divide our searching complexity by half. In other words if everytime we are looking for data that is less than data in our root node we will traverse to the left of the tree and this eliminates the right side of a tree cutting the search by half. And vice-versa if data is higher we eliminate the left side everytime.

## **Recursions**
Recursion means that the function is calling itself and repeating this behavior until some conditions are met in order to return a result. This is a great thing to know when we are using BST.    
Steps of recursion:
- find small and simple problems
- Find a base case which doesn't require recursion     
```python
#this function is calling itself recursively infinitely or until
# a recursionerror occurs
```Without Recursion Base case```
def recursion():
    print("recursion forever")
    recursion()# this is a recursive call

recursion()
#to fix the infinite recursion we follow the steps of recursion mentioned above
#We first find the minimum number of recursion and that is our smaller problem
``` With recursion Base case```
def recursion(allow_recursion):
    if allow_recursion <= 0: #do nothing (base case)
        return
    else:
        print("recursion forever")
        recursion(allow_recursion-1) # smaller problem
recursion(20)
```
Notice how without stating the number of recursions the top code function calls itself infinitely and the second code has a limit which allows it to stop somewhere and return the result.

## **Operations in BST**
You might have wondered why all of a sudden we included a basic understanding of how recursion works. The reason is that in order to insert into a BST we use recursion.
We still follow the same recursion step:
- Smaller problem: This is when we are inserting a value on the left or the right subtree based on the value.
- Base Case: If we find an empty space to a add the node, we have found a right spot to add the item.     

Inserting into a BST requires that we first find out if the root node is empty. if it is empty we plug the user value in that root node. if it is already occupied we check the occupant and determine whether we need to go right or left. We repeat the process either on the left or right, hence recursive call.
