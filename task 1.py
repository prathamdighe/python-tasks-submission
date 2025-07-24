
def factorial(num):
    if num<2:
        return 1
    else:
        return num * (factorial(num-1))

r=int(input("Enter a number: "))

result= factorial(r)

print("Factorial of ",r,"is:",result)