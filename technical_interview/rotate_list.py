def rotate(array,n):
    rotate_result = array[-n:]
    unrotate_result = array[:len(array) - n]
    print(rotate_result + unrotate_result)
rotate([1, 2, 3, 4, 5], 2)