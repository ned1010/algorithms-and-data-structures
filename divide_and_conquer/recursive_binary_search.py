
def binary_search(sorted_array, left, right, target):

    if left >= right:
        return "value not found"

    middle_index = ( left + right )//2
    middle_value = sorted_array[middle_index]
    #base case
    if target == middle_value:
        return middle_index

    #recursive steps
    if middle_value > target:
        return binary_search(sorted_array, left, middle_index, target)
    if middle_value < target:
        return binary_search(sorted_array, middle_index+1, right,target)

    
    
# test cases
#takes only sorted list
array = [5,6,7,8,9]
print(binary_search(array, 0, len(array), 10))
