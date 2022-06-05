#tree is also a recursive data structure

def buildbst(lst):

    if len(lst) == 0:
        return None

    middle_index = len(lst)//2
    middle_value = lst[middle_index]

    tree_node = {"data": 10}
    tree_node["left_subtree"] = buildbst(lst[:middle_index])
    tree_node["right_subtree"] = buildbst(lst[middle_index+1:])

    return tree_node

print(buildbst([1, 5, 3, 9, 1, 9, 12]))

