#Hashing taking a key of the something and providing a key-value store using an array
#key: is the identifier
#hash function: that takes input and returns hash code of the key
#compression function: transforms inputs to some smaller range of index of the array

# if there is a collision(that is hash function returns same number such that two inputs have same output)
# we need to account for collision
class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]
    
    def hash_function(self, key, collision_count=0):
        #must return some number/hash code
        #it is a irreversible process
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + collision_count

    def compress_function(self, hash_code):
        #use modulo to find index by array length
        return hash_code % self.array_size


    def assign(self, key, value):
        #this should put the value to the array
        array_index = self.compress_function(self.hash_function(key))
        current_array_value = self.array[array_index]

        #if the current index in the array is empty, we add the new key-value pair
        if current_array_value is None:
            self.array[array_index] = [key, value]
            return 
        
        #collision
        #if there is a collision, we need to find the new hash
        num_collisions = 1
        while(current_array_value[0] != key):
            new_array_index = self.compress_function(self.hash_function(key, num_collisions))
            current_array_value = self.array[new_array_index]

            if current_array_value[0] is None:
                self.array[current_array_value] = [key, value]
                return 
            
            if current_array_value[0] == key:
                self.array[current_array_value] = [key, value]
                return

            num_collisions += 1

        return

    def retrieve(self, key):
        #retrieve the value using the key
        array_index = self.compress_function(self.hash_function(key))
        return_value = self.array[array_index]
        
        #[key, value] this how data is stored, so first index is key and second is value
        if return_value is None:
            return None
        if return_value[0] == key:
            return return_value[1]


        #collision retrieve
        retrival_collision = 1

        while(return_value[0] != key):
            new_array_index = self.compress_function(self.hash_function(key, retrival_collision))

            new_array_value = self.array[new_array_index]

            if new_array_value is None:
                return None
            if new_array_value[0] == key:
                return new_array_value[1]

            retrival_collision += 1
        return 


hashmap = HashMap(10)

hashmap.assign("Nidup", 19)
hashmap.assign("Sonam", 30)
hashmap.assign("thinkel", 5)

print(hashmap.retrieve("Nidup"))
print(hashmap.retrieve("Sonam"))
print(hashmap.retrieve("Key"))