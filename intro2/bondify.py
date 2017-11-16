'''
When you run a function:
1. Memory is allocated for the function
2. Variables created / used in a function are "local" to the funciton
   they get their values in the function and don't affect variables
   using the same name in the main program or other functions
When a function returns:
1. memory for the function, including local variables is freed and goes away


'''
def myfirstfunc():
    print("I'm in the function")
    print("I'm still in the function")
    

def f():
    x = 30
    print(x)
    f2()
    print(x)

def f2():
    x = 50
    print(x)
    
def bondify(full_name):
    sloc = full_name.find(" ")
    last = full_name[sloc+1:]
    intro_string = last + ", " + full_name
    return intro_string

myfirstfunc()
print("----------------------")
myfirstfunc()

x = 20
print(x)
f()
print(x)

intro = bondify("Roger Moore")
print(intro)
print(bondify("Ian Flemming"))
      