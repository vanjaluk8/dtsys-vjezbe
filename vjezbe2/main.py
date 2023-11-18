# PYTHON FUNCTIONS
# write a function that prints a message "Dobrodošli u Python"
def welcome():  # function definition
    print("Dobrodošli u Python")

print(welcome())  # function call


def ciao(name, time_of_day):
    print(f'Ciao {name}, {time_of_day}')

print (ciao('Ivan', 'Dobro jutro'))

# wirte a function that calculates the factorial of a number
def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result

print(factorial(5))

# write a function that acts as a simple calculator (+, -, *, /). the function should take two numbers and an operand as entry and return the result    
def calculator(num1, num2, operand):
    if operand == '+':
        return num1 + num2
    elif operand == '-':
        return num1 - num2
    elif operand == '*':
        return num1 * num2
    elif operand == '/':
        return num1 / num2
    else:
        return 'Invalid operand'
    
print (f'Rezultat: {calculator(5,3,"+")}')

# write a function that takes two variables and calculates the sum and difference. The function must return the sum and difference for the returned value
def calculate(num1, num2):
    return print(f'Jedan smjer: {num1 + num2}, Drugi smjer: { num1 - num2}')

print(f'Rezultat: {calculate(5,3)}')

##################### LAMBDA FUNCTIONS
# write a lambda function that multiplies two numbers
multiply = lambda x, y: x * y
print(multiply(5,3))

kvadrat = lambda x: (2*x**2) + (3*x +1)
print(f'Lambda kvadrat: {kvadrat(5)}')

### LAMBDA USAGE
# write a function primjena_lambde. This function has to take two argument
# 1. lambda_function - that will be used on every number from the list
# 2. list_of_numbers - on which the function will be used
# the function should return prerfom the operation on every number and return a new list with the results

kvadrat = lambda x: (x**2)
def primjena_lambde(kvadrat, list_of_numbers):
    return [kvadrat(i) for i in list_of_numbers]

lista = [i for i in range(0,11)]
print(lista)

print(primjena_lambde(kvadrat, lista))
