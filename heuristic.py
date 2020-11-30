import csv
import numpy as np
reader = csv.reader(open("MenuIngredients.csv"))

ingredients = next(reader)[1:]
print(ingredients)

matrix = []

for row in list(reader):
	matrix.append([c!="" for i,c in enumerate(row[1:])])
	
print(matrix)
	
matrix = np.array(matrix).T
cost = np.array([1 for i in range(len(matrix[0]))])

from setcover import SetCover
g = SetCover(matrix, cost)#, maxiters=100, subg_nsteps=20, subg_maxiters=200)
solution, time_used = g.SolveSCP()
print(solution)
print(g.s)

#solution = g.greedy()
#print(solution)

test = [False for i in range(len(matrix[0]))]

matrix = matrix.T
for i,s in enumerate(g.s):
	if s:
		print(ingredients[i])
		for xi, x in enumerate(matrix[i]):
			if x:
				test[xi] = True

print(test)
print(all(test))

print()
