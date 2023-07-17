#Bubble sort membandingkan 2 data yang berdekatan
#menukarkan posisi sesuai dengan urutanya

def BubbleSort(data):
    x = len(data)
    for i in range(x-1):
        for j in range(0, x - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

x = [10,5,9,2,20,11,2,3,15]
print("Sebelum Sort : ", x)
BubbleSort(x)
print("Setelah Sort : ", x)
