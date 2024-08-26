try:
    a = int(input("Enter any Number"))
    b = int(input("Enter any Number"))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Denominator can't be 0")
except ValueError:
    print("Input should be an integer")
except:
    print("Something went wrong")