import csv

reader = csv.reader(open("MenuIngredients.csv"))

ingredients = next(reader)[2:]
print(ingredients)

things = {}

for row in list(reader):
	things[row[0]] = {i for i,c in enumerate(row[2:]) if c!=""}

print(len(ingredients))
mcover = set()
cover = set()
while len(cover) != len(ingredients):

	mx = max(things.items(), key=lambda thing:thing[1]-cover)
	cover = cover.union(mx[1])
	mcover.add(mx[0])
	print(len(cover), len(mcover), cover, mcover)

test = [False for i in range(len(ingredients))]
for ingredient in mcover:
	for x in things[ingredient]:
		test[x] = True

print(", ".join(mcover))
print(len(mcover))

#print(test)
print(all(test))
