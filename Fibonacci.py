def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

#Time Complexity = O(2^n)
#Space Complexity = O(n)

def fibonacci_iterative(n):
    if n<=1:
        return n
    a,b = 0,1
    for _ in range(2,n+1):
        a,b = b, a+b
    return b
#Time Complexity = O(n)
#Space Complexity = O(1)

n = int(input("Enter the value of n: "))
print("Fibonacci Number of using recursive method: ",fibonacci_recursive(n))
print("-------------------")
print("Fibonacci Number of using recursive method: ",fibonacci_iterative(n))
