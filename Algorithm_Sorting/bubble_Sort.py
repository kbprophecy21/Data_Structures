def bubbleSort(arr):
    n = len(arr)

    #Traverse through all array elements
    for i in range(n-1):
        #range(n) also work but outer loop will 
        # repeat one time more than needed.
        #Last i elements are already in place.
        for j in range (0, n-1):


            #traverse the array from 0 to n-i-1
            #Swap if the element found is greater
            #than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [45, 45, 44, 66, 3245, 235, 45, 634, 2, 5 ,63, 6, 36 ,663,63, 776, 765, 754, 885, 8, 5, 3, 2, 78, 65, 34, 23, 54, 75, 74 ]

bubbleSort(arr)




