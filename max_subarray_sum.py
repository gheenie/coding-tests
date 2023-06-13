def max_sequence(arr):
    max_sum = 0
    # current_sum = arr[0]
    
    for subarray_length in range(1, len(arr) + 1):
        current_sum = sum(arr[:subarray_length])
        
        if current_sum > max_sum:
            max_sum = current_sum
        
        for i in range(len(arr) - subarray_length):
            current_sum -= arr[i]
            current_sum += arr[i + subarray_length]
            
            if current_sum > max_sum:
                max_sum = current_sum
    
    return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# Should be 6: [4, -1, 2, 1]
