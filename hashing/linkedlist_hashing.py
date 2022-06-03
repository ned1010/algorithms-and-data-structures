from linkedlist import Node, LinkedList
from flowers import flower_definitions
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key, value])
    #this is teh linked list in the array
    list_at_array = self.array[array_index]
    #overwrite the value
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
        return
    list_at_array.insert(payload)


  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    #list_at_index gives me linklist object at a given index
    list_at_index = self.array[array_index]
    #saving the value
    for item in list_at_index:
      if item[0] == key:
        return item[1]
      return None

blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  key, value = flower[0], flower[1]
  blossom.assign(key, value)
print(blossom.retrieve("sunflower"))
