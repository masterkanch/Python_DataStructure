import time
import random

# Python3 Program for recursive binary search.

# Returns index of x in arr if present, else -1


def binarySearch(arr, l, r, x):

    print(l, r)  # to slow down the program

    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Driver Code
if __name__ == "__main__":
    # input size
    n = 1000

    # randomly generate list in order
    arr = []
    for i in range(n):
        a = random.randint(-1000, 1000)
        arr.append(a)
        arr.sort()
    arrMax = max(arr)
    arrMin = min(arr)
    #print(arrMax, arrMin, arr)

    # search target
    x = random.randint(arrMin, arrMax+1)
    print("x = ", x)

    start_time = time.time()
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")

    stop_time = time.time()
    print("input size = ", len(arr))
    print("start time = ", start_time)
    print("stop_time = ", stop_time)
    print("diff_time = ", (stop_time - start_time), "seconds.")
