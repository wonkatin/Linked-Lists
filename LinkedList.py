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
    # check if the list is empty first to avoid bugs
    if self.is_empty(): return None
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

  # return the sum of all the values in the linked list
  def sum(self):
    # a varaible to hold the running total
    total = 0
    # start at the begginning of the list
    current_node = self.head
    while current_node != None:
      # add value of current node to total 
      total += current_node.value
      # keep the iteration going
      current_node = current_node.next
    # return the sum
    return total

  # return a [list] (regular python list) from all the values in the linked list
  def to_list(self):
    # list to store all the values
    li = []
    # start at the begginning of the linked list
    current_node = self.head
    while current_node != None:
      # append value of current node to li
      li.append(current_node.value)
      # keep the iteration going
      current_node = current_node.next
    # return the li
    return li

  # search for a given value in the list. 
  # If it is found, return True otherwise return False
  def search(self, value):
    # loop over list looking for the value
    current_node = self.head
    while current_node != None:
      # if the value is found, return True
      if current_node.value == value: return True
      # keep the loop going 
      current_node = current_node.next
    # otherwise, return false
    return False
  
  # add a node with the given value to the beginning of the list
  # this doesn't need a loop -- remember the head is the beginning 
  # of the list. unshift should return the new length of the list
  def unshift(self, value):
     # create a new node with the given value
    new_node = Node(value)
    # set the next of the new node to be the current head
    new_node.next = self.head 
    # set head to the newly created node
    self.head = new_node 

  # reomve the value at beginning of the list
  def shift(self):
    # store the current head in a variable to be returned
    removed_head = self.head 
    # set the head to be the next of the head
    self.head = self.head.next 
    return removed_head

