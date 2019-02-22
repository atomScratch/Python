fibolist = [0,1]
currentpos = 1
result = 0
while True:
    fibolist.append(int(fibolist[currentpos - 1] + fibolist[currentpos]))
    currentpos += 1
    if fibolist[currentpos] > 3999999:
        break
    if (fibolist[currentpos] % 2) == 0:
        result += fibolist[currentpos]
print(fibolist)
print(result)
