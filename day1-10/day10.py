import day10_art

logo = day10_art.logo
operations = {
    '+' : 'add',
    '-' : 'sub',
    '/' : 'div',
    '*' : 'mul'
}
flag = 'y'

def add(n1, n2):
    ''' Add two numbers and returns them'''
    return n1 + n2

def sub(n1, n2):
    ''' Subtracts two numbers and returns them'''
    return n1 - n2

def div(n1, n2):
    ''' Divides two numbers and returns them'''
    return n1 / n2

def mul(n1, n2):
    ''' Multiplies two numbers and returns them'''
    return n1 * n2

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Enter an operation from the lines above: ")
calc_function = operations[operation_symbol]
answer = eval(calc_function + "(num1, num2)")
print(f"{num1} {operation_symbol} {num2} = {answer}")

while flag == 'y':
    operation_symbol = input("Pick another operation: ")
    new_number = float(input("Enter another number: "))
    calc_function = operations[operation_symbol]
    new_answer = eval(calc_function + "(answer, new_number)")
    print(f"{answer} {operation_symbol} {new_number} = {new_answer}")
    flag = input("Type 'y' to continue calculating with {new_answer} or type 'n' to exit: ")

