def max_sequence(arr):
    max_sum = 0
    
    for i in range(len(arr)):
        j = i
        current_sum = 0

        while j != len(arr):
            current_sum += arr[j]
            
            if current_sum > max_sum:
                max_sum = current_sum
            
            j += 1
    
    return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# Should be 6: [4, -1, 2, 1]


# def max_sequence(arr):
#     max_sum = 0
    
#     for subarray_length in range(1, len(arr) + 1):
#         current_sum = sum(arr[:subarray_length])
        
#         if current_sum > max_sum:
#             max_sum = current_sum
        
#         for i in range(len(arr) - subarray_length):
#             current_sum -= arr[i]
#             current_sum += arr[i + subarray_length]
            
#             if current_sum > max_sum:
#                 max_sum = current_sum
    
#     return max_sum


# def max_sequence(arr):
#     max_sum = 0

#     subarray_length = 1
#     current_sum = 0
#     i = 0
#     is_traversing_right = True

#     while subarray_length != len(arr) + 1:
#         if is_traversing_right:
#             current_sum += arr[subarray_length - 1]
#         else:
#             current_sum += arr[i - subarray_length + 1]

#         if current_sum > max_sum:
#             max_sum = current_sum

#         if is_traversing_right:
#             while i != len(arr) - subarray_length:
#                 current_sum -= arr[i]
#                 current_sum += arr[i + subarray_length]

#                 if current_sum > max_sum:
#                     max_sum = current_sum

#                 i += 1

#             i = len(arr) - 1
#         else:
#             while i != subarray_length - 1:
#                 current_sum -= arr[i]
#                 current_sum += arr[i - subarray_length]

#                 if current_sum > max_sum:
#                     max_sum = current_sum

#                 i -= 1

#             i = 0

#         is_traversing_right = not is_traversing_right
#         subarray_length += 1
    
#     return max_sum
