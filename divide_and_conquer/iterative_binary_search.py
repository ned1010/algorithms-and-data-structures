def binary_search(array, target):
    left_pointer = 0
    right_pointer = len(array)

    while left_pointer < right_pointer:
        middle_index = (left_pointer + right_pointer)//2
        middle_value = array[middle_index]


        #this will return the value
        if middle_value == target:
            return middle_index
        
        if target < middle_value:
            right_pointer = middle_index
        
        if target > middle_value:
            left_pointer = middle_index+ 1

    return "target not found"


# test cases
#takes only sorted list
print(binary_search([5,6,7,8,9], 7))
print(binary_search([5,6,7,8,9], 9))
print(binary_search([5,6,7,8,9], 8))
print(binary_search([5,6,7,8,9], 4))
print(binary_search([5,6,7,8,9], 6))