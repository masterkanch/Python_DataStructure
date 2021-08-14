#633040206-5 Kanch Ruansiripiyakul
count = 0
def digits(x):
    global count
    if(x!=0):
        count=count+1
        return digits(x//10)
    return count

number_pb4 = int(input("Enter a positive integer: "))
print(f"{number_pb4} has {digits(number_pb4)} digits(s)")