def sum_mix(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return sum(arr)




print(sum_mix([9, 3, '7', '3']))