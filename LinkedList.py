from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def update(self,key,value):
    current_node = self.head
    found = False
    counter = 0

    while current_node != None and not found:
      if current_node.data[0] == key:
        current_node.data = (current_node.data[0],current_node.data[1]+1)
        found = True
      else:
        current_node = current_node.next
        counter +=1



  def find(self,item):

    current = self.head

    found = False
    counter = 0

    while current != None and not found:

      if current.data == item:
        found = True
      else:
        current = current.next
        counter += 1

    if found:
      return counter
    else:
      return -1



  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    current = self.head
    
    if current == None:
      print('The linked list is empty.')
    else:
      for i in range(self.length()):
        print(f'Node {i}: {current.data}')
        current = current.next