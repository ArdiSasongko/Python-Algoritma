def quick_sort(nums):
    x = len(nums)
    if x < 1:
        return nums

    pivot = nums[len(nums)//2]
    left = [ i for i in nums if i < pivot]
    middle = [ i for i in nums if i == pivot]
    right = [i for i in nums if i > pivot]

    return quick_sort(left) + middle + quick_sort(right)

list = [4, 1, 12, 5, 3, 2, 9, 6, 11, 10, 8, 7]
print("Before sort:", list)
sorted_list = quick_sort(list)
print("After sort:", sorted_list)