n=int(input("Enter the range of number:"))
x=int(input("Enter the value of x:"))
sum=0
i=1
while(i<=n):
    sum+=x/i
    i+=2
print("The sum of the series = ",sum)