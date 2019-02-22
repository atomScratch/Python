import string
alphabet = list(string.ascii_lowercase)

while True:
    outputlist = []
    outputstring = ""
    inputstring = list((input("Input String: ")).lower())
    inputshift = input("Input Shift: ")
    for x in range(len(inputstring)):
        if inputstring[x] in list(" 01234567890!@#$%^&*(),."):
            outputlist.append(inputstring[x])
        else:
            outputlist.append((alphabet.index(inputstring[x]) + int(inputshift)) % 26)
    for x in range(len(outputlist)):
        if outputlist[x] in list(" 01234567890!@#$%^&*(),."):
            outputstring = outputstring + outputlist[x]
        else:
            outputstring = outputstring + alphabet[outputlist[x]]
    print(outputstring)
