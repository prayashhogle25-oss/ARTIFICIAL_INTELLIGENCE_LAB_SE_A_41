n=int(input("enter the number whose factorial you want to find:"))
fact=1
for i in range(1,n+1):
	fact=fact*i
	
print("the factorial of the no :",n,"is",fact)
