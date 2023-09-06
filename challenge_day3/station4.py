def solution_station_4(x):
    output = "True"

    if x == 1:
        output = "False"
    elif x <= 3:
        output = "True"
    elif x % 2 == 0 or x % 3 == 0:
        output = "False"
    else:
        i = 5
        while i * i <= x:
            if x % i == 0:
                output = "False"
                break
            i += 2

    return output


x = 61
print(solution_station_4(x))


def solution_station_6(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(solution_station_6(50))
