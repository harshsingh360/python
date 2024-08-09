nterms=int(input("Enter how many terms you want of fibonacci series : "))
t1=0
t2=1
counter=0
print("Fibonacci Series : ")
while(counter<nterms):
    print(t1)
    t=t1+t2
    t1=t2
    t2=t
    counter=counter+1
