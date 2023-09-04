from elli import get_name as get_name_elli
from yash import get_name as get_name_yash
from felix import get_name as get_name_felix

def team_names():
  print("This is Team Bike to the Future. We are:")

elli_name = get_name_elli()
yash_name = get_name_yash()
felix_name = get_name_felix()

print(f" - {elli_name}")
print(f" - {yash_name}")
print(f" - {felix_name}")

if __name__ == "__main__":

  team_names()
