def skip_and_sum(n):
    total_sum = 0
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            continue
        total_sum += i
    
    return total_sum
n = 10 
result = skip_and_sum(n)
print("Sum of numbers from 1 to", n, "skipping even numbers:", result)