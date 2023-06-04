#Create fibonacciGenerator() to create a generator for Fibonacci series
def fibonacciGenerator():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b
    
#Create multipleBy(n) to create a generator for multiples of 1 to 100 by n
def multipleBy(n):
    for i in range(1, 101):
        yield i * n

#Create exponentialBy(n) to create a generator for exponents of 1 to 100 by n
def exponentialBy(n):
    for i in range(1, 101):
        yield i ** n

#Test case for question 1
fibonacci = fibonacciGenerator()
print(next(fibonacci)) 
print(next(fibonacci)) 
print(next(fibonacci)) 
print(next(fibonacci)) 
print(next(fibonacci)) 
print(end = '\n')

#Test case for question 2
multiply = multipleBy(5)
print(next(multiply)) 
print(next(multiply)) 
print(next(multiply)) 
print(next(multiply)) 
print(end = '\n')

#Test case for question 3
exponential = exponentialBy(3)
print(next(exponential)) 
print(next(exponential)) 
print(next(exponential)) 
print(next(exponential)) 