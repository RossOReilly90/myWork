import re

print("\nCalculator")
print("\nType 'quit' to exit\n")

previous = 0
run = True

def perform_math():
    global run
    global previous
    equation = ""
    
    if previous == 0:
        equation = input("Enter equation: ")
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        #while equation == '':
            #equation = input("Enter equation please: ")
        #return equation   
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Thank you, goodbye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
            
while run:
    perform_math()