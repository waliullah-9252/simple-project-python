# summatin function
def summatin(a,b):
    r = a + b
    return r

# subtraction function
def subtraction(a,b):
    r = a - b
    return r

# multiply function
def multiply(a,b):
    r = a * b
    return r

# division function
def division(a,b):
    if b == 0:
        return 'Error! Divide by zero is not allowed'
    else:
        r = a / b
        return r
    

# calcultor function
def calcultor_app():
    print('Welcome to the calcultor application')
    print('Select the operator')
    print('1. Summation')
    print('2. Subtraction')
    print('3. Multification')
    print('4. Division')

    choice = input('Enter choice (1/2/3/4): ')

    if choice in ('1', '2', '3', '4'):
        a = float(input('Enter a number: '))
        b = float(input('Enter b number: '))

        if choice == '1':
            print("Summation is ", summatin(a,b))
        elif choice == '2':
            print("Subtraction is ", subtraction(a,b))
        elif choice == '3':
            print("Multification is ", multiply(a,b))
        elif choice == '4':
            print("Division is ", division(a,b))

    else:
        print('Invalid input! Please valid input is (1/2/3/4)')


# calculator functions call
calcultor_app()