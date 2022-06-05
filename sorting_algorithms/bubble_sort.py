#bubble sort uses two loops to iterate through

def bubble_sort(lst):
    #element in the lst
    for element in lst:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
my_list = [5, 2, 0, 1, 3]

print("Pre-Sort: {0}".format(my_list))      
sorted_list = bubble_sort(my_list)
print(sorted_list)
