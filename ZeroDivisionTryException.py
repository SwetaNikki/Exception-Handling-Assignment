"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

def divide(x,y):
    return x/y
        
try:
    divide(5/0)
except ZeroDivisionError:
    print("Exception: Division by zero!!")
except:
    print("Any other exception")
    
