def solution_station_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return solution_station_1(n - 1) + solution_station_1(n - 2)

n = 97
result = solution_station_1(n) 
print(f"The {n}th term of the Fibonacci sequence is: {result}")
