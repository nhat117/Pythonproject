try :
    number = int(input("Enter a number\n"))
    print(value)
except ZeroDivisionError as err:
    print(err)
except TypeError :
    print("Invalid input")