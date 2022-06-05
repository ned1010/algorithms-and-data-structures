
from random import randrange, shuffle

def quick_sort(lst, start, end):
    
    #base case
    if start > end:
        return


    #using last element as pivot
    pivot_element = lst[end]    

    # #using random element as pivot
    # pivot_index = randrange(start, end+1)
    # pivot_element = lst[pivot_index]

    # #put the pivot at the last of the list
    # lst[end], pivot_element = pivot_element, lst[end]

    lesser_than_pointer = start

    for i in range(start, end+1):
        if lst[i] < pivot_element:
            lst[lesser_than_pointer], lst[i]= lst[i], lst[lesser_than_pointer]
            lesser_than_pointer += 1
    
    lst[end], lst[lesser_than_pointer] = lst[lesser_than_pointer], lst[end]

    quick_sort(lst, start, lesser_than_pointer-1)
    quick_sort(lst, lesser_than_pointer + 1, end)

  
list = [5,3,1,7,4,6,2,8]
shuffle(list)
print("PRE SORT: ", list)
#subtract 1 from the len(list) because we are using zero index
quick_sort(list, 0, len(list)-1)
print("POST SORT: ", list)

