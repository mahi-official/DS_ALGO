def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter Number\n"))
f = factorial(n)
for i in range(1,n+1):
    print(fibonacci(i), end=' ')
print("Factorial of {} is: ".format(n), f)

