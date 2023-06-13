def max_sequence(arr):
    max_sum = 0
    
    for subarray_length in range(2, len(arr) + 1):
        for i in range(len(arr) - subarray_length + 1):
            current_sum = sum(arr[i:i + subarray_length])
            if current_sum > max_sum:
                max_sum = current_sum
    
    # Possible optimisation: subtract front element, add next element
    # current_sum
    
    return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# Should be 6: [4, -1, 2, 1]
