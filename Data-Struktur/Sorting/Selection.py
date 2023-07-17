#selection sort membandingkan dengan nilai terkecil
def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_number = i
        for j in range(i+1, n):
            if data[j] < data[min_number]:
                min_number = j
        data[i], data[min_number] = data[min_number], data[i]


x = [10,5,9,2,20,11,2,3,15]
print("Sebelum Sort : ", x)
selection_sort(x)
print("Setelah Sort : ", x)