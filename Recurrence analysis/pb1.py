import time


def facRec(n):
    print(n, end=" ")
    if n == 1:
        print()
        return 1
    return n * facRec(n-1)


def facLoop(n):
    fac = 1
    for i in range(1, n+1):
        print(i, end=" ")
        fac *= i
    print()
    return fac


if __name__ == "__main__":

    # input size
    n = 100

    start_time = time.time()
    result = facLoop(n)
    stop_time = time.time()
    print("Factorial Loop:")
    print("Result = ", result)
    print("start time = ", start_time)
    print("stop_time = ", stop_time)
    print("diff_time = ", (stop_time - start_time), "seconds.")
    start_time = time.time()
    result = facRec(n)
    stop_time = time.time()
    print("Factorial Recursion:")
    print("Result = ", result)
    print("start time = ", start_time)
    print("stop_time = ", stop_time)
    print("diff_time = ", (stop_time - start_time), " seconds.")
