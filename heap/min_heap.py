

class MinHeap:

    def __init__(self):
        self.heap_list = [None]
        self.count = 0
    
    #helper function
    def parent_idx(self, idx):
        return idx//2

    def left_child(self, idx):
        return idx * 2

    def right_child(self, idx):
        return idx * 2 + 1


    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify()
    
    def heapify(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            if child < parent:
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child

            #this gives the index of parent node
            idx = self.parent_idx(idx)
            print("heap restored {0}".format(self.heap_list))

min_heap = MinHeap()

random_list = [3, 5, 10, 2, 1]
for element in random_list:
    min_heap.add(element)
print(min_heap.heap_list)