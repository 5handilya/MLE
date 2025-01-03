import random,time
m = 128 
n = 256 
o = 128 
A = [[random.random() for i in range(n)] for j in range(m)]
B = [[random.random() for i in range(o)] for j in range(n)]
C = [[0 for i in range(o)] for j in range(m)]
start_time = time.time()
for i in range(m):
	for j in range(o):
		for k in range(n):
			C[i][j] += A[i][k] * B[k][j]
print(time.time() - start_time)
