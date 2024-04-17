#Task 1: Create functions for each arithmetic operation

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0: #If else statement if user input for b is zero, creates error message
        return 'Error, Try Again!'
    else: return a / b

def multiply(a, b):
    return a * b

#Task 2: Implement user input to receive numbers as an operation choice

print(''' 
     Calculator App 
''')
print('Select Operation:')
print('1. Add')
print('2. Subtract')
print('3. Divide')
print('4. Multiply')

while True:
    choice = input('Enter 1/2/3/4: ')

    if choice in ('1','2','3','4'):
        num1 = int(input('Enter 1st Number: '))
        num2 = int(input('Enter 2nd Number: '))
    if choice == '1':
        print('Result: ', add(num1, num2))
    elif choice =='2':
        print('Result ', subtract(num1, num2))
    elif choice == '3':
        print('Result ', divide(num1, num2))
    elif choice == '4':
        print('Result ', multiply(num1, num2))


    else:
        print('Invalid Input') #Task 3: Program can handle division by zero and other potential errors
    