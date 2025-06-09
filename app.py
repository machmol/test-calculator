import operations as op

while True:
    try:
        numberOne = input("\nfirst number > ")
        operator = input("operation: +, -, * , /, % >")
        if operator not in ['+', '-', '*', '/', '%']:
            print('unknown operator, please start over.')
            continue
        numberTwo = input("second number > ")

        if operator == "+":
            print(op.plus(numberOne, numberTwo))
        elif operator == "-":
            print(op.minus(numberOne,numberTwo))
        elif operator == "*":
            print(op.multiple(numberOne,numberTwo))
        elif operator == "/":
            if numberTwo == "0":
                print('I cant devide by 0, please start over:')
                continue
            print(op.division(numberOne, numberTwo))
        elif operator == "%":
            print(op.modulo(numberOne,numberTwo))
        
        again = input('do you wanna try again? (y/n)')
        if again != 'y':
            break
    
 
    except ValueError:
        print('invalid Input, please start over. \n')