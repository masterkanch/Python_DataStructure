#633040206-5 Kanch Ruansiripiyakul

#Problem3
def sum(number):
    if number <= 1:
        return 1
    else:
        return number + sum(number - 1)

def display_sum(number):
    for count in range(1,number+1):
        print(sum(count))
        if count == number:
            print(f"Sun of 1 to {number} is {sum(count)}")

#Problem4
count = 0
def digits(x):
    global count
    if(x!=0):
        count=count+1
        return digits(x//10)
    return count

if __name__ == '__main__':
    number_pb3 = int(input("Enter an integer: ")) 
    display_sum(number_pb3)
    number_pb4 = int(input("Enter a positive integer: "))
    print(f"{number_pb4} has {digits(number_pb4)} digits(s)")