def insertion_sort(nums):
    n = len(nums)
    for i in range(1,n):
        x = nums[i]
        y = i-1
        while y >= 0 and nums[y] > x:
            nums[y + 1] = nums[y]
            y -= 1
        nums[y + 1] = x

x = [10,5,9,2,20,11,2,3,15]
print("Sebelum Sort : ", x)
insertion_sort(x)
print("Setelah Sort : ", x)