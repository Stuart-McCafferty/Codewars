def sum_two_smallest_numbers(numbers):
    min_1 = min(numbers)
    min_1_index = numbers.index(min_1)
    del(numbers[min_1_index])
    min_2 = min(numbers)
    min_2_index = numbers.index(min_2)
    del(numbers[min_2_index])
    return min_1 + min_2