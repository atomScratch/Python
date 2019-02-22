'''I don't know why you are looking at this, one would expect
someone on github to already know how to do this.'''
mult1 = int(input("Multiple 1: "))
mult2 = int(input("Multiple 2: "))
for currentval in range(1,101):
    ftest = currentval % mult1 == 0
    btest = currentval % mult2 == 0
    if (ftest and btest) == True:
        print("FizzBuzz")
    elif (ftest == True):
        print("Fizz")
    elif (btest == True):
        print("Buzz")
    else:
        print(currentval)
        
          
    
