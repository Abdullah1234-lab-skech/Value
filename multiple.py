try:
    mum1, num2= eval(input("Enter two numbers separated by a comma:")) 
    result= mum1/num2 
    print("The result is :" , result) 
except ZeroDivisionError:
    print('Division by zero is error !') 
except SyntaxError: 
    print('Comma is missing') 
except: 
    print('wrong input') 
else:
    print('No exceptions') 
finally:
    print('Execution completed')