
import felix
import elli
import yash

e = elli.get_name()
f = felix.get_name()
y = yash.get_name()

a = felix.paragrpah_one_felix


d = felix.paragrpah_two_felix


g = felix.paragrpah_three_felix


def team_names():
    return f"This is Team Bike to the Future. We are: {f}, {e}, {y}"


if __name__ == "__main__":
    team_name = team_names()
    print(team_name)
