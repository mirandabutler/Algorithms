#HW 1: Selection Sort Algorithm-Miranda Butler
	#CPU: 64-bit, 8 CPUs
	#OS: Linux
	#memory size: 1 Terabyte
	#10^3 ~ 0.0399s
	#10^4 ~ 3.89s
	#10^5 took too long, since last one increased by a factor of 2 (*100), 
		#since its quadratic (2 for loops) I would guess this one to be about 4*10^4s 
	#10^6 based on the trend this would be about 4*10^8s 

#import 
from random import randint
import timeit

#define variables

def sorts(n):

#define variables 
	rands =[]
	runTime=[]

	
	for x in range (1,11):
		#start timer
		start = timeit.default_timer()

		#generate random ints
		for y in range(0,n):
			new = randint(0,10*n) 
			rands.append(new)

		#sort array
		for i in range(len(rands)):
		    for j in range(i, len(rands)):
		        if(rands[i] > rands[j]):
		            rands[i], rands[j] = rands[j], rands[i] #swaps elements 

		
		#end timer
		stop = timeit.default_timer()
		runTime.append(stop-start)
		print "Sorted List %s: %s" %(x,rands)
		# reset array variable
		rands = []
	
	#print running time(min, max and average)  
	for x in range(0,10):
		for y in range(x,10):
			if runTime[y]<runTime[x]:
				minRunTime = runTime[y]
			else:
				minRunTime=runTime[x]
			if runTime[y]>runTime[x]:
				maxRunTime= runTime[y]
			else:
				maxRunTime=runTime[x]
	
	#output results 
	print "Max run time is %s" %(maxRunTime)
	print "Min run time is %s" %(minRunTime)
	averageRunTime = (maxRunTime+minRunTime)/2	
	print "Average run time is %s" %(averageRunTime)



#user input 
n = input("Input number of integers you want to generate: ")
sorts(n)
