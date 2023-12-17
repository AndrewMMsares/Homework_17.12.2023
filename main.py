print("Hello user")
print("Please enter a number from 1 to 7 and we will display the day of the week")
numb = None
while numb is None:
    try:
            numb = int(input("Nunber: "))
            match  numb:
                case 1:
                    print("Monday")
                case 2:
                    print("Tuesday")
                case 3:
                    print("Wednesday")
                case 4:
                    print("Thursday")
                case 5:
                    print("Friday")
                case 6:
                    print("Saturday")
                case 7:
                    print("Sunday")
    except ValueError:
        print("Enter a number from 1 to 7 without letters")
    finally:
        print("Thank you for using our program.")
