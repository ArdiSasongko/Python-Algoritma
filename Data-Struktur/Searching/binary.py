import bisect

data = [2,4,5,7,11,12,14,16,17,18,21,22,24,25]

#membuat binary seacrh
def binary_search(nums,x):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

print("List :", data)
x = int(input("Masukan angka yang ingin dicari : "))
pos = binary_search(data, x)
print("Menggunakan binary search manual")
print(f"Posisi {x} berada pada {pos}")
print(" ")
pos = bisect.bisect_left(data,x)
print("Menggunakan library bisect untuk binary search")
print(f"Posisi {x} berada pada {pos}")