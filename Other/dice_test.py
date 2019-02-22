import random
while True:
    diesize = input("How large would you like your die to be: ")
    diceroll = random.randrange(0,diesize,1)
    print "Your rolled a: " + str(diceroll)
