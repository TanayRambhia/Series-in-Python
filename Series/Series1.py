num = int(input("How many terms?"))
res = 0
fact = 1
     
for i in range(1, num+1):
    fact *= i
    res = res + (i/ fact)
print(res)