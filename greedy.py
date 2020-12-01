import csv

reader = csv.reader(open("MenuIngredients.csv"))

dishes = next(reader)[2:]
ingredients = []

print("dishes", dishes, len(dishes))

rows = list(reader)
columns = []

for row in rows:
	ingredients.append(row[0])

for ci in range(len(rows[0])-2):
	columns.append([])
	for row in rows:
		columns[-1].append(row[2+ci])
#print(ingredients)

things = {}
for ci, column in enumerate(columns):
	things[dishes[ci]] = {i for i,c in enumerate(column) if c!=""}

print(things)

mcover = set()
cover = set()
while len(cover) != len(ingredients):
	mx = max(things.items(), key=lambda thing:thing[1]-cover)
	cover = cover.union(mx[1])
	mcover.add(mx[0])
	print(len(cover), len(mcover))
	print(cover, mcover)

test = [False for i in range(len(ingredients))]
for dish in mcover:
	for x in things[dish]:
		test[x] = True

print(", ".join(mcover))
print(len(mcover))

#print(test)
print(all(test))
