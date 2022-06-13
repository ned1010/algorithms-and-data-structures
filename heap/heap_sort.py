#heap sort is an algorithm which uses heap to sort elements
#it inserts data into heap and extract the root of the heap. 
#time complexit of (n log n)

from max_heap import MaxHeap

def heap_sort(lst):
    result = []
    max_heap = MaxHeap()

    for element in lst:
        max_heap.add(element)

    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        result.insert(0, max_value)
    return result
#Testing out
my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heap_sort(my_list)
print(sorted_list)