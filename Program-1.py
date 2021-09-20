"""

Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

"""


class Person:
    def __init__(self, a, b, type_of_operation):
        
        self.int_1 = int_1
        self.int_2 = int_2
        self.type_of_operation = type_of_operation
        
        # Addition
        if (type_of_operation == '+'):
            print (a + b)
        
        # Subraction    
        if (type_of_operation == '-'):
            print (a - b)
        
        # Multiplication    
        if (type_of_operation == '*'):
            print (a * b)
        
        # Division    
        if (type_of_operation == '/'):
            if (b != 0):
                print (a / b)
            else:
                print ("Anything cannot be divided by Zero") 

    
a = float(input())
b = float(input())
type_of_operation = str(input())
p1 = Person(a, b, type_of_operation)

