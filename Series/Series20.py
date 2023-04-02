n=int(input("Enter the range of number:"))
sum=0
for i in range(1,n+1):
    sum+=pow(i,3)
print("The sum of the series = ",sum)