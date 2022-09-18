def insertion_sort(L):
    for i in range(len(L)):
        for j in range(0, i):
            if (L[i] < L[j]):
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L


L = [15, 63, 68, 16, 37, 22]
print("The unsorted list is: ", L)
print("The sorted list is: ", insertion_sort(L))
