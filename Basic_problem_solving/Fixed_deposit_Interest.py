principal=float(input("enter the principal amount :"))
rate=float(input("enter the annual interest rate(%): "))
year=1
while year <=5:
    principal= principal*(1+rate*100)
    print(year,principal)
    year+=1
