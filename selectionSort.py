# Selection sort
def selection_sort(nums: list) -> list:
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(smallest_idx, len(nums)):
            if nums[smallest_idx] > nums[j]:
                smallest_idx = j
        nums[smallest_idx], nums[i] = nums[i], nums[smallest_idx]
    return nums
