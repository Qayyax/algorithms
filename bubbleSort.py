# Bubble sort

def bubble_sort(nums: list) -> list:
    for i in nums:
        for j in range(len(nums)-1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
