sum_result = 0
for x in range(1,1000):
   if (x % 3) == 0:
       sum_result += x
   elif (x % 5) == 0:
       sum_result += x
   print("Current sum equals: " + str(sum_result))

print(sum_result)
