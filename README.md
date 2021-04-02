# ⛓ Linked List ⛓

## We are going to be building a new data type: the `linked list!` 🎉

This particular specimen will be of the `singly linked list` variety.

 The super cool thing about linked lists are that there are always *more cool and fun* methods to add and challenges to solve. 
 
 We are going to cover the basics of how a linked list works and setup some basic methods to manage the data inside of it.

![mr links](/linky-stinky.png)

A linked list consists of two classes: the main `LinkedList` class that stores all the methods and a reference to the `head` of the list (the first thing in it). The other class is a `Node` that stores a data value and the reference to the next node.

Since the `LinkedList` class only knows about the the `head Node`, we have to zip across the list by starting at the head and asking each node what the next node is.

#### In this repo:

There is a `LinkedList` Class and `Node` in the file 'LinkedList.py` that we are going to build out together.

The `LinkedList` class is being imported into `list_testing.py` so we can try out our linked list easier.

## We Do:

Build a linked list!

```python
# ## # ## # ## # ## 
# A single node of data in our list
class Node:
  def __init__(self, value):
    # the value of this node
    self.value = value
    # a reference to the next node
    self.next = None
  
  # for printing
  def __repr__(self):
    return self.value

# ## # ## # ## # ## 
# the linked list 'manager' class
class LinkedList:
  def __init__(self):
    # a reference to the first node
    self.head = None
    # the current size of the list (-1 will mean empty)
    self.length = -1

  # check if list has nodes and return a boolean
  def is_empty(self):
    return self.length == -1

  # add node to end of list and return the new length of the list
  def append(self, value):
    # create a new node from given value 
    new_node = Node(value)
    # check if the list is empty
    if self.is_empty():
      # if so, set the new node to be the head 
      self.head = new_node
    else:
      # start at the head of the list
      current_node = self.head
      while current_node.next != None:
        # update the current node to point to the next node
        current_node = current_node.next
      # update the next node to be the current node
      current_node.next = new_node
    
    # increment length
    self.length += 1
    return self.length
  
  # remove the last node in the list and return it
  def pop(self):
    # keep track of the previous node to nullify it
    previous_node = None
    # start from the head
    current_node = self.head
    # loop to the end of the list
    while current_node.next != None:
      # set the previous node
      previous_node = current_node
      # set the current node
      current_node = current_node.next
    
    # set previous_node's next to None
    previous_node.next = None
    # decrement the length of the list
    self.length -= 1
    # return the removed node
    return current_node

  # print the values of our list
  def __repr__(self):
    # string to return
    list_string = ''
    # start at the head of the list, loop over all the nodes
    current_node = self.head
    index = 0
    while current_node != None:
      list_string += f'{index}: {current_node.value}\n'
      # go to the next node
      current_node = current_node.next
      # increment index
      index += 1 
  
    return f'List Length: {self.length}\n{list_string}'

  # make our linked list work with len()
  def __len__(self):
    return self.length
```

## You Do:

Finish building out the rest of the methods in the `LinkedList` class

### Methods that need a loop

To finish these methods, you will have to loop across the linked list.

```python
  # return the sum of all the values in the linked list
  def sum(self):
    pass

  # return a [list] (regular python list) from all the values in the linked list
  def to_list(self):
    pass

  # search for a given value in the list. 
  # If it is found, return True otherwise return False
  def search(self, value):
    pass
```

### Methods that don't need a loop:

These methods don't need a loop to be completed, and both deal with operations on the `head node` of the list.

```python
  # add a node with the given value to the beginning of the list
  # this doesn't need a loop -- remember the head is the beginning 
  # of the list. unshift should return the new length of the list
  def unshift(self, value):
    pass

  # reomve the value at beginning of the list
  def shift(self):
    pass
```

### If you finish these

Try to think of other methods that could trick out your linked list.

*examples : a method to replace a insert a node at a certain index or a for_each method that does a callback on every node in the list*