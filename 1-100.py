maximum = int(input("Please enter the Maximum Value: "))

number = 1
while number<= maximum:
    if(number % 2 != 0):
        print("{0}".format(number))
    number = number + 1