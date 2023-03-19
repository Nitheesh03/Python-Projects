print("Welcome to Arithmetic Calculator!!!!")
def main():
    a=int(input("Enter the first number:"))
    b=int(input("Enter your second number:"))

    print("Choose any one of the calculation!")

    x=['Add','Sub','Multiply','Divide']

    for i in x:
        print(i)
    y=input("Enter the operand:")
    if y=='Add':
        c=a+b
        print("Addition:")
        print(c)
    elif y=="Sub":
        c=a-b
        print("Subtractio:")
        print(c)
    elif y=='Multiply':
        c=a*b
        print('Multiplication:')
        print(c)
    elif y=='Divide':
        c=a/b
        print("Division:")
        print(c)
    else:
        print("Try different operand!")
    repeat=input("Would you like to try again? y/n:")
    if repeat=='y':
        main()
    else:
        print("Thank You! Have a nice day!!")
    exit()
main()


    



       
