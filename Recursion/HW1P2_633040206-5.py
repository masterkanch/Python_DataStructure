def reverse(array):
    if len(array) == 0:
        return array
    return [array[len(array)-1]] + reverse(array[0:len(array) - 1])

def printarray(array):
    for i in array:
        print(i,end=" ")

n = int(input("Enter a list size: "))
alist = list(map(int,input(f"Enter {n} integers:").split()))

print(f"Order list:", end=" ")
printarray(alist)
print()
print(f"Reversed list:",end = " ")
printarray(reverse(alist))

