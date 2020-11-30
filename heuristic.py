import csv
import numpy as np
reader = csv.reader(open("MenuIngredients.csv"))

ingredients = next(reader)[2:]
print(ingredients)

matrix = []

for row in list(reader):
	matrix.append([c!="" for i,c in enumerate(row[2:])])

#print(matrix)
print(len(matrix), "rows", len(matrix[0]), "columns")
matrix = np.array(matrix)

cost = np.array([1 for i in range(len(matrix[0]))])

from setcover import SetCover
g = SetCover(matrix, cost, maxiters=1000, subg_nsteps=100, subg_maxiters=300)
solution, time_used = g.SolveSCP()
print(solution)
print(matrix)
print("solution", g.s, len(g.s))

#solution = g.greedy()
#print(solution)

test = [False for i in range(len(matrix))]

matrix = matrix.T
for i,s in enumerate(g.s):
	if s:
		print(ingredients[i])
		#print(matrix[i])
		for xi, x in enumerate(matrix[i]):
			if x:
				test[xi] = True

print(len(g.s))
#print(test)
print(all(test))

#for row in matrix:
#	print(" ".join(["1" if x else "0" for x in list(row)]))
