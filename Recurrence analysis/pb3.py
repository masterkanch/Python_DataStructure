import time
import random

# Python program for implementation of MergeSort


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        print(mid)  # to slow the program down

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    # input size
    n = 100

    # randomly generate list in order
    arr = []
    for i in range(n):
        a = random.randint(-1000, 1000)
        arr.append(a)

    #print("Given array is", end="\n")
    # printList(arr)

    start_time = time.time()
    mergeSort(arr)
    stop_time = time.time()

    #print("Sorted array is: ", end="\n")
    # printList(arr)

    print("input size = ", len(arr))
    print("start time = ", start_time)
    print("stop_time = ", stop_time)
    print("diff_time = ", (stop_time - start_time), " seconds.")

# This code is contributed by Mayank Khanna
