# ## # ## # ## # ## 
# A single node of data in our list
class Node:
  # constructor
  def __init__(self, value):
    #value of node
    self.value = value
    # reference to the next node
    self.next = None
  # method override for printing
  # like __str__ but you can use any data type
  def __repr__(self):
    return f'{self.value}'

# test_node = Node('test string node')
# print(test_node)


# ## # ## # ## # ## 
# the linked list 'manager' class
class LinkedList:
  def __init__(self):
    # a reference to the head(first node)
    self.head = None
    # keep track of size of linked list
    self.length = -1

  # helper function that checks if the linked list is empty
  def is_empty(self):
    return self.length == -1 #returns true if it's true

  # add a node to the end of the list
  # return the new length
  def append(self, value):

    # create new node from given value
    new_node = Node(value)

    # check if list is empty, make new node the head if so
    if self.is_empty():
      self.head = new_node
    else:
      # loop to the end of the linked list 
      # start at beginning and go till find 'none'
      current_node = self.head
      while current_node.next != None:
        current_node = current_node.next

      # set the last node's next to be the new node
      current_node.next = new_node
      # print(current_node) # check for debugging

    # increment self.length
    self.length += 1
    
    # return self.length
    return self.length

  # remove last node from end of the list
  # return what we removed
  def pop(self):
    # check if the list is empty -- if so, return None
    if self.is_empty():
      return None
    # keep track of the previous node and current node while we loop
    previous_node = None
    current_node = self.head
    while current_node.next != None:
      # update the previous node 
      previous_node = current_node
      
      # update the current node 
      current_node = current_node.next

      # after we find the end set the previous node.next to be None
    previous_node.next = None

      # decrease the length
    self.length -= 1
      # return the node we removed
    return current_node # the one that no longer lives in our linked list

  # print the linked list
  def __repr__(self):
    # string to return
    list_string = ''
    # loop over the whole list
    current_node = self.head
    index = 0
    while current_node != None:
      # add value of each node to our return string
      list_string += f'{index}: {current_node.value}\n'
      index += 1
      # go to the next node
      current_node = current_node.next
    #return the string
    return list_string
    





  # return the sum of all the values in the linked list
  def sum(self):
    # variable for sum of all values
    node_sum = 0
    #start the loop at the head
    current_node = self.head
    while current_node != None:
      #add value to running total
      node_sum += current_node.value
      # go to the next node
      current_node = current_node.next
    return node_sum

  # return a [list] (regular python list) from all the values in the linked list
  def to_list(self):
    pass

  # search for a given value in the list. 
  # If it is found, return True otherwise return False
  def search(self, value):
    pass
  
  # add a node with the given value to the beginning of the list
  # this doesn't need a loop -- remember the head is the beginning 
  # of the list. unshift should return the new length of the list
  def unshift(self, value):
    pass

  # remove the value at beginning of the list
  def shift(self):
    pass

