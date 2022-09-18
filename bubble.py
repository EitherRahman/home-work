def bubble_sort(L):
    for i in range(0, len(L) - 1):
        for j in range(len(L) - 1):
            if (L[j] > L[j + 1]):
                temp = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temp
    return L


L = [125, 63, 682, 126, 37, 222]
print("The unsorted list is: ", L)
print("The sorted list is: ", bubble_sort(L))
import time

st = time.time()
sum_x = 0
for i in range(1000000):
    sum_x += i
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
