n = int(input())
countries = set()
for i in range(0,n):
    countries.add(input())
print(countries)
count = 0
for i in countries:
    count += 1
print(count)