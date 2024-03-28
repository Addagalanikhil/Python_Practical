def remove_duplicates(nums):
    if not nums:
        return 0
    
    slow_ptr = 0
    for fast_ptr in range(1, len(nums)):
        if nums[fast_ptr] != nums[slow_ptr]:
            slow_ptr += 1
            nums[slow_ptr] = nums[fast_ptr]

    return slow_ptr + 1

nums = [0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7]
length = remove_duplicates(nums)
print("Length after removing duplicates:", length)
print("Modified array:", nums[:length])
