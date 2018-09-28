import random

n=4
source = [1,3,5]
destin = [11,10,13]
t_row = []       # top row
b_row = []       # bottom row
l_col = []       # left column
r_col = []       # right column

for i in range(1,n+1):
    t_row.append(i)
for i in range(n*(n-1)+1, n*n+1):
    b_row.append(i)
for i in range(1,n*(n-1)+2,n):
    l_col.append(i)
for i in range(n,n*n+1,n):
    r_col.append(i)
print(t_row,b_row,l_col,r_col)    


def generate_path(sodist):
	path=[]
	kk=0
	# for i in 
	i=sodist[0]
	path.append(sodist[0])
	while 1:
		kk+=1
		if kk==30: #to exit infinite loop
			print("time out")
			return -1
			break
		if sodist[1] in path:
			break
		else:
			if i in t_row:
				if i==1:
					tt=random.choice([i+1,i+n])
					if tt not in path:
						path.append(tt)
						i=tt
				elif i==n:
					tt=random.choice([i-1,i+n])
					if tt not in path:
						path.append(tt)
						i=tt
				else:
					tt=random.choice([i+1,i-1,i+n])
					if tt not in path:
						path.append(tt)
						i=tt
			elif i in b_row:
				if i==n*(n-1)+1:
					tt=random.choice([i+1,i-n])
					if tt not in path:
						path.append(tt)
						i=tt
				elif i==n*n:
					tt=random.choice([i-1,i-n])
					if tt not in path:
						path.append(tt)
						i=tt
				else:
					tt=random.choice([i-1,i+1,i-n])
					if tt not in path:
						path.append(tt)
						i=tt
			elif i in l_col:
				tt=random.choice([i+n,i-n,i+1])
				if tt not in path:
					path.append(tt)
					i=tt
			elif i in r_col:
				tt=random.choice([i+n,i-n,i-1])
				if tt not in path:
					path.append(tt)
					i=tt
			else:
				tt=random.choice([i+1,i-1,i+n,i-n])
				if tt not in path:
					path.append(tt)
					i=tt
			# print(path)		
	# print(path,"final")																					


	return path



def initialize():
    population = []
    for _ in range(10):
        chromosome = []
        for i in range(len(source)):
        	xx=generate_path(list(zip(source,destin))[i])
        	if xx!=-1:
        		chromosome.append(xx)	
            
        population.append(chromosome)
    return population

def show(population):
    for chromosome in pop:
        print(chromosome,"chromosome")
        print('')

pop = initialize()
show(pop)
