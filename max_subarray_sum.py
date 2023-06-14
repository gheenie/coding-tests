def max_sequence(arr):
    best_sum = 0
    current_sum = 0
    
    for x in arr:
        # Reset the front pointer of the subarray whenever its sum goes negative
        # to the next positive num
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    
    return best_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# Should be 6: [4, -1, 2, 1]
