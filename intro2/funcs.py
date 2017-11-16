'''
parameters are declared in the () of the function definition
(separated by commas if more than one).

They are like local variables but get their initial value from the caller


'''

def f(hamster):
    print('f:',hamster)
    hamster = hamster * 2
    print('f:',hamster)
    

def doubler(x):
    '''
return imediately ends the function you are running and goes back to the
caller. If you return a value, like 2*x here in the return statement, that
value is sent back and can be used in the caller
'''
    newvalue = 2*x
    # print(newvalue)
    return  newvalue 




x=10
print('main:', x)
f(x)
print('main:',x)

f(30)

print("---------------------------------------")

x = 100
x = doubler(x)
print(x)