def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    left_half = merge_sort(left)
    right_half = merge_sort(right)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

list = [4, 1, 12, 5, 3, 2, 9, 6, 11, 10, 8, 7]
print("Before sort:", list)
sorted_list = merge_sort(list)
print("After sort:", sorted_list)
