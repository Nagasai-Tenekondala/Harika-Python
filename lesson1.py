# In python everything is an object
# Functions are firstclass members in python

def add(num1:int, num2:int)-> any:
    "This function is used to add two numbers give as arguments"
    sum = num1  + num2
    print(f'Addition of two numbers {num1} ,{num2} is {sum}')

# type hint

def sample(test:int, population:int,*args, **kwargs):
    print(test)
    print(population)



def mean(*args):
    sum = 0
    for i,item in enumerate(args):
        sum +=item
    average = sum/len(args)
    print(average)