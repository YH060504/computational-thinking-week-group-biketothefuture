def solution_station_6(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(solution_station_6(50))
