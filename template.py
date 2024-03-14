#IO OPTIMISATIONS
import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline().strip

#IMPORTS
#from itertools import combinations
from bisect import bisect_right as br

#IO TEMPLATES
def yn(n):
    print("YES" if n else "NO")
def ilist():
    return [int(i) for i in input().split()]
def silist():
    return sorted([int(i) for i in input().split()])
def rilist():
    return sorted([int(i) for i in input().split()],reverse=True)
def mint():
    return map(int,input().split())

#SNIPPETS
xtill=lambda x: [x,1,x+1,0][x%4] 

#STANDARD ALGORITHMS
def primes(u):
    prime=[None,None]+[True]*(u-1)
    for i in range(2,len(prime)):
        if prime[i]:
            for j in range(i,u//i+1):
                prime[i*j]=False
    return prime
prime=[None,None]
#prime=primes(10**6)

def primer(a):
    if a == 1:
        return tuple()
    if prime[a]:
        return (a,)
    for i in primes:
        if i*i>a:
            break
        else:
            if a%i==0:
                return (i,) + primer(a//i)

#DATA STRUCTURES
class Graph():
	def __init__(self, nodes):
		self.V = nodes
		self.graph = [[0 for column in range(nodes)]
					for row in range(nodes)]
	def mIndex(self, dist, sptSet):
		min = float("inf")
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v
		return min_index
	def djikstra(self, src):
		dist = [float("inf")] * self.V
		dist[src] = 0
		sptSet = [False] * self.V
		for cout in range(self.V):
			u = self.mIndex(dist, sptSet)
			sptSet[u] = True
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]
		return dist

################################################################
################################################################
################################################################
################################################################
def solve():
    #MANOGYA SINGH 2024

    return

################################################################
################################################################
################################################################
################################################################
    
ts=1
ts=int(input())
for t in range(ts):
    solve()
