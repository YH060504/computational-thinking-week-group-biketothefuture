
# X = station number
def solution_station_3(number):
  if number % 3 == 0:
    output = "True"
  else:
    output = "False"
  return output

number = 57217
print (solution_station_3(number))
number = 75212
print (solution_station_3(number))