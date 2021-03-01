from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.



  def create_arr(self, size):
     
    new_arr = []

    for i in range(size):
      ll = LinkedList()
      new_arr.append(ll)
    return new_arr




  # 2️⃣ TODO: Create your own hash function.

  #simple hash function that divides the total amount of keys by 
  # the size of the array and assign the new item a value/position in the array


  def hash_func(self, key):
    
    return len(key) % self.size


  # 3️⃣ TODO: Complete the insert method.



  def insert(self, key, value):
    new_item = (key,value)
    #setting the new_items key(word) to the proper index
    arr_index = self.hash_func(key)
    #linked list created at array index
    ll = self.arr[arr_index]
    found = False
    pointer = ll.head
    #loops through the array and checks if the key exist 
    while pointer is not None:
      if pointer.data[0] == key:
        found = True
      pointer = pointer.next

    if found:
      ll.update(key,value)
    else:
      ll.append(new_item)








    




  # 4️⃣ TODO: Complete the print_key_values method.


  def print_key_values(self):
    for ll in self.arr:
      ll.print_nodes()



