import time

n = int(input("Enter a number: "))

start = time.time()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(n)

end = time.time()

print("Factorial:", result)

execution_time = end - start
print("Execution Time:", execution_time, "seconds")

print("Time Complexity: O(n)")
