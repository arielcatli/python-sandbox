#Demo global variables

global_variable = 3.14
GLOBAL_CONSTANT = 9

def number():
    global global_variable  #use the globa variable instead
    global_variable = 2     #shadows global variable
    print(global_variable)
    print(GLOBAL_CONSTANT)

number()
print(global_variable)

print("This is a along code. A very long line of code", \
      " that does only a printing task.")