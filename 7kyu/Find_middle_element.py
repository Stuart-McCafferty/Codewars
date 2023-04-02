def gimme(input_array):
    array = list(input_array)
    array.pop(array.index(max(array)))
    array.pop(array.index(min(array)))
    return input_array.index(array[0])
