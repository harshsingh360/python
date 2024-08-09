principle=int(input("Enter the principle amount : "))
rate = int(input("Enter the rate : "))
time = int(input("Enter the time : "))

amount=principle*((1+(rate/100))**time)
print("The compound interest is : ",amount)
