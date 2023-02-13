def number3(number1_,number2_):
    if number1_ > number2_:
        print(f"The bigger number is {number1_}")
    if number2_ > number1_:
            print(f"The bigger number is {number2_}")
    if number1 == number2:
            print("The number is equal")

while True:
    try:
        number1 = int(input(":enter the first number:"))
        number2 = int(input(":enter the second number:"))
        if number1 != 0 and number2 != 0:
            print("Valid numbers")
            number3(number1,number2)
    finally:break