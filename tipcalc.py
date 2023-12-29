#user input

total = input("what is your total bill?\n")
tip = input("do you want to tip 10%, 12%, or 15%\n")
split = input("how many ways are we spliting this bill?\n")

#calculations
a = float(tip) / 100
b = float(total) * a
final = round ((float(total) + float(b)) / int(split), 2)
print (f"your total bill is {final}")
print (a)
print (b)
