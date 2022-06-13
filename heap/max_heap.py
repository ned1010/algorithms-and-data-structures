#heaps are special tree structure that is complete binary
#max-heap -> parent is larger than children

class MaxHeap:
    def __init__(self):
        #this is the list of heap
        self.heap_list = [None]
        #this keeps track of the indices of the node
        self.count = 0
    
    #helper functions
    def parent_index(self, index):
        return index//2
    def left_child(self, index):
        return index * 2
    def right_child(self, index):
        return index * 2 + 1

    def child_present(self, index):
        return self.left_child(index) <= self.count

    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        #correct any violation of the max-heap/priority queue
        self.heapify()

    #while adding if the max-property is violated, we need to fix that
    #we will use heapify method to do use
    def heapify(self):
        #count gives the index of the element
        #We set idx to self.count to get the index value of the last element.
        idx = self.count
        #as long as the child has a parent
        while self.parent_index(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_index(idx)]

            if parent < child:
                #swap the nodes
                self.heap_list[idx] = parent
                self.heap_list[self.parent_index(idx)] = child
            #you can loop through the whole depth of the tree until 
            #we reach the root of tree
            #the loop terminates when the it reaches the root.
            idx = self.parent_index(idx)
        print("heap restored {0}".format(self.heap_list))


    def retrieve_max(self):
        if self.count == 0:
            print("No element in the heap")
            return None
        #equating max value to the first element
        max_value = self.heap_list[1]
        print("Removing " + str(max_value) + " from the" + str(self.heap_list))
        #replace the first element with the last element 
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print("Last element moved to first: {0}".format(self.heap_list))
        #rebalance the tree
        self.heapify_down()

        return max_value


    def heapify_down(self):
        #since we poped the root the largest
        #and swapped with the last element
        #we need to rebalance it
        idx = 1

        while self.child_present(idx):
            print("heapying down")
            larger_index = self.get_the_larger_index(idx)
            print(larger_index)
           
            #parent has two options to swap either left or right child
            #so use get_the_larger_index to get the largest_index
            child = self.heap_list[larger_index]
            parent = self.heap_list[idx]

            if parent < child:
                self.heap_list[idx] = child
                self.heap_list[larger_index] = parent
            idx = larger_index

        print("Heap Restored! {0}".format(self.heap_list))
        print("")
    
    def get_the_larger_index(self, idx):
        #base case
        if self.right_child(idx) > self.count:
            print("There is only one child")
            return self.left_child(idx)
        else:
            left_child = self.heap_list[self.left_child(idx)]
            right_child = self.heap_list[self.right_child(idx)]

            if left_child > right_child:
                print(f"Left child " + str(left_child) + " is greater than the right child " + str(right_child))
                return self.left_child(idx)
            else:
                print(f"Right child " + str(right_child)+ " is greater than left child " + str(left_child))
                return self.right_child(idx)

# heap = MaxHeap()

# random_list = [3, 5, 10, 2, 1, 10, 12, 5, 6]
# for element in random_list:
#     heap.add(element)
# print(heap.heap_list)
