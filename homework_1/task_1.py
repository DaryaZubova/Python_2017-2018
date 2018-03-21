def fib(n):
    fib_numbers = [1, 1]
    for i in range(2, n):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers[-1]


for i in range(1, 20):
    print(fib(i))
