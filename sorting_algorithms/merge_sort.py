def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    middle_index = len(lst)//2
    #this divides the list into smaller sections
    left_sort = merge_sort(lst[:middle_index])
    right_sort = merge_sort(lst[middle_index:])

    return merge(left_sort, right_sort)

def merge(left, right):
    result = []

    #as long as there exists value in the right and left
    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)


    if left:
        result += left
    if right:
        result += right

    return result
    


#Testing out
my_list = [5, 2, 3, 1, 1, 0]

print("Pre-sort {0}".format(my_list))
sorted_list = merge_sort(my_list)
print(sorted_list)