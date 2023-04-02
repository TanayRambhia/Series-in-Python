n=int(input("Enter the range of number:"))
sum_series=0
i=1
while(i<=n):
    multiply=1
    for j in range(1,i+1):
        multiply*=j
    sum_series+=multiply
    i+=1
print("The sum of the series = ",sum_series)