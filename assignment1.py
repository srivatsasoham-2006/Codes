# 1️⃣ Calculator Program (Basic Arithmetic)
# What this program does
# A calculator program performs basic mathematical operations such as:
# Addition
# Subtraction
# Multiplication
# Division
print("Enter the Number: ")
a=float(input())
b=float(input())
print("Choose operation:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")
choice=input("Enter the choice(+,-,*,/):")
if choice=='+':
  print(a+b)
elif choice=='-':
  print(a-b)
elif choice=='*':
  print(a*b)
elif choice=='/':
  if(b==0):
    print("Invalid Input")
  else:
    result=a/b
    print(a/b)
else:
  print("Invalid Input")
