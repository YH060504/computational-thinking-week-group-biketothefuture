
import felix
import elli
import yash
import diana

e = elli.get_name()
f = felix.get_name()
y = yash.get_name()
d = diana.get_name()


def team_names():
    return f"This is Team Bike to the Future. We are: {f}, {e}, {y}"


if __name__ == "__main__":
    team_name = team_names()
    print(team_name)
== == == =


def team_names():
    return f"This is Team Bike to the Future. We are: {f}, {e}, {y}, {d}"


if __name__ == "__main__":
    team_name = team_names()
    print(team_name)
>>>>>> > c74ffe7a09cf6534f062b8ac5ebabb19cf3bf394