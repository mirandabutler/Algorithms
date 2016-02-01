#HW: 5 
	#Miranda Butler 100619710

import sys 
import math 


def main(argv):
	l = wordlist(argv)
	m = adj_matrix(l)
	s = sources(m)
	path = dfs(m,s)
	longestPath(path,l)
	


#---------------------------------------------------------------------------------------------------------------------
#read/write to wordlist
#---------------------------------------------------------------------------------------------------------------------
def wordlist(argv):	
	#read file
 	wordList = []
	f = open(sys.argv[1], "r")
	
	#write file to list
	for line in f:
		wordList.append(str.strip(line))
	f.close()
	return wordList


#---------------------------------------------------------------------------------------------------------------------
#create adjacency matrix
#---------------------------------------------------------------------------------------------------------------------
def adj_matrix(wordList): #create a nxn matrix
	#initialize adjacency matrix	
	size = len(wordList)
	adjMAT = [[0]*size for i in range(size)]
	

	#search wordList/fill adjacency matrix
	for i in range(size):
		wordi = wordList[i]

		for j in range(size):
			wordj = wordList[j]
			if len(wordi)==len(wordj)-1:
				#compare words 
				count =0
				for c in wordi:
					for x in wordj:
						if c==x:
							count+=1
							wordj=wordj.replace(x,"",1)
							break

				if count == len(wordi):
					#update adjacency matrix
					adjMAT[i][j]=1
					

	# #check
	# for i in range(len(adjMAT)):	
	# 	print adjMAT[i]
	# print adjMAT
	return adjMAT	

#---------------------------------------------------------------------------------------------------------------------
# find longest chain of words
#---------------------------------------------------------------------------------------------------------------------
def sources(adjMAT):
	size = len(adjMAT)
	source =[]
	for i in range(size):
		val = 0
		for j in range(size):
			val = adjMAT[j][i]
			if val==1:
				break
		if val==0:
			source.append(i) 

	#returns list of indices of sources (indices correspond to wordlist) 
	return source 



def dfs(MAT,s):
	#Define Variables
	size = len(MAT)
	finalpath = []
	
	#iterte through source list 
	for i in s:
		#initialize/re-initialize
		path = []
		curr_path=[]
		start=i
		visited, stack = set(), [start]
		temppath =[]
		prev=0
		while stack: #while stack is not empty 
			vertex =stack.pop()
			if vertex not in visited and vertex>=prev: #add vertex to visited
				prev=vertex
				visited.add(vertex)
				temppath.append(vertex)
				for j in range(1,size):
					if MAT[vertex][j]==1: 
						stack.extend([vertex,j])

		#save to path array 
		if path is None:
			path.append(temppath)
			curr_path = temppath
		elif len(temppath)>=len(curr_path):
			path.append(temppath)
			curr_path=temppath

		finalpath.append(path)
			
	return finalpath


		
		

def longestPath(path,wordlist):
	path1 = []
	path2 = []
	path3 = []
	end =len(path)-1
	for i in path[0][0]:
		path1.append(wordlist[i])
	print path1 
	for i in path[1][0]:
		path2.append(wordlist[i])
	print path2 
	for i in path[3][0]:
		path3.append(wordlist[i])
	print path3 
	return




#---------------------------------------------------------------------------------------------------------------------
# main entry point
#---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main(sys.argv)
	



#try using  dctionary and starting at the last word and initialize with  
#sparse matrix 