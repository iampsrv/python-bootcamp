while(1):
    try:
        x=int(input("Enter the value of x"))
        y=int(input("Enter the value of y"))
        a=x/y
        print("the value of a is ",a)
    except ZeroDivisionError as e:
        print("Dont give the value of y zero")
    else:
        print("No exception occured")
    finally:
        print("Division operation completed")