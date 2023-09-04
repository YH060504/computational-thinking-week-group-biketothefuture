from elli import get_name as get_name_team_member_1
from yash import get_name as get_name_team_member_2
from felix import get_name as get_name_team_member_3

def team_names():
  print("This is Team Bike to the Future. We are:")

name_team_member_1 = get_name_team_member_1()
name_team_member_2 = get_name_team_member_2()
name_team_member_3 = get_name_team_member_3()

print(f" - {name_team_member_1}")
print(f" - {name_team_member_2}")
print(f" - {name_team_member_3}")

if __name__ == "__main__":
  team_names()
