
def solution_1(n):
    return n * (n + 1) / 2
    
def solution_2(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i
        i = i + 1

    return sum

print(solution_1(10))
print(solution_2(10))
        