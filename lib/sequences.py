#!/usr/bin/env python3

def print_fibonacci(n):
    fibonacci_sequence = []
    a, b= 0,1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a,b = b,a+b
    print(fibonacci_sequence)
    
print_fibonacci(100)

