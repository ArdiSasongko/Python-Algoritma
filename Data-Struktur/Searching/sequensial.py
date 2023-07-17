import random
#membuat sequensial search
def sequensial_search(nums,x):
    for i,item in enumerate(nums):
        if item == x:
            return i
    return -1

data = [4,1,12,66,12,100,2,45,17,13]

print("List :", data)
x = int(input("Masukan angka yang ingin dicari : "))
pos = sequensial_search(data, x)
print("Menggunakan sequensial search")
print(f"Posisi {x} berada pada {pos}")