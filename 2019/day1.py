import math

lines = open("day1.txt", "r").read().split()

def calc_fuel(mass, sum=0):
    fuel = math.floor(mass/3) - 2
    print(type(fuel))
    print(sum)
    if fuel <= 0:
        return sum
    else:
        sum += fuel
        return calc_fuel(fuel, sum)

sum = 0
for line in lines:
    if line:
        line = int(line.strip())
        fuel = calc_fuel(line)
        sum += fuel

print(sum)


