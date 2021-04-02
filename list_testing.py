# ## # ## # ## # ##
# testing area for our linked list
from LinkedList import LinkedList

our_list = LinkedList()

print(our_list.is_empty())

print(our_list.pop())

our_list.append(1)
our_list.append(2)
our_list.append(3)
our_list.append(4)

print(our_list)

our_list.pop()

print(our_list)

print(len(our_list))

print(our_list.sum(), 'sum')
print(our_list.to_list(), 'to_list')

print(our_list.search('pink elephants'))
print(our_list.search(2))

our_list.unshift('why is it called unshift?')
print(our_list)
print(our_list.shift())


