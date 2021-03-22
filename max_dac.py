from random import randint

def max_dac(arr):
    # if the length of the array is 0, raise the ValueError
    if len(arr) == 0:
        raise ValueError("The list has to have one element at least")
    # if the length of the array is 1, return the value the array has 
    if len(arr) == 1:
        return arr[0]
    # if the length of the array is 2, return the greater one
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    # divide the array in half and recur this function
    divider = len(arr)//2
    max_1 = max_dac(arr[:divider]) if divider > 1 else arr[0]
    max_2 = max_dac(arr[divider:])

    # return the greater one
    return max_1 if max_1 > max_2 else max_2


# create an array which size is 10 and values are between -10000 and 10000 
arr = [randint(-10000, 10000) for _ in range(10)]

# print the created array and the maximum value
print("The input array: ", arr)
print("The maximum value: ", max_dac(arr))