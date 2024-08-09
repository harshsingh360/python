#sum of digits
n=int(input("Enter the no: "))
s=0
while(n!=0):
    r=n%10
    s=s+r
    n=n//10
print("Sum = ",s)

#reverse a number code with the above code with only one change
n=int(input("Enter the no: "))
s=0
while(n!=0):
    r=n%10
    s=s*10+r   #Here is the change
    n=n//10
print("Reverse of a number = ",s)


n=int(input("Enter the no: "))
s=0
while(n!=0):
    r=n%10
    s=s*10+r   #Here is the change
    n=n//10
print("Reverse of a number = ",s)
