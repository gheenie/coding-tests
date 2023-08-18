class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        self.merge_sort(nums)

        for i, num in enumerate(nums):
            # For when you reach the last number
            if i == len(nums) - 1: return False
            if num == nums[i + 1] : return True

    def merge_sort(self, arr):
        # Stop condition
        if len(arr) > 1:
            # Split the array into two halves
            mid = len(arr) // 2
            sub_array1 = arr[:mid]
            sub_array2 = arr[mid:]
 
            # Recursively sort the two halves
            self.merge_sort(sub_array1)
            self.merge_sort(sub_array2)
         
            # Initial values for pointers that we use to keep track of where we are in each array
            i = j = k = 0
 
            # Pick the smaller number between the two subarrays until just one is fully traversed
            while i < len(sub_array1) and j < len(sub_array2):
                if sub_array1[i] < sub_array2[j]:
                    arr[k] = sub_array1[i]
                    i += 1
                else:
                    arr[k] = sub_array2[j]
                    j += 1
                k += 1
 
            # Append the rest of the numbers from the part-traversed subarray. This is where the optimisation happens
            while i < len(sub_array1):
                arr[k] = sub_array1[i]
                i += 1
                k += 1
 
            while j < len(sub_array2):
                arr[k] = sub_array2[j]
                j += 1
                k += 1
