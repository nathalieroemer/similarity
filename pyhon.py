
""" Fibonacci Folge bis 100
a=0
 b=1
## alternativ: a,b = 0,1
 while a < 100:
    print(a)
      a,b = b, a+b
"""
""" doesnt work - why??
x = int(input("Please enter an integer:  "))
if x < 0:
    x=0
    print('Negative value changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('One')
else:
    print('More than one')
    """



""" games = ['Dictator', 'Ultimatum', 'Trust', 'Public Good']
for g in games:
    print(g, len(g)) """

def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b=b, a+b
fib(2000)


def add(a,b): ## defines the function
    print('a is', a)
    print('b is', b)
    print(a + b)
add(5, 6) ##executes the function