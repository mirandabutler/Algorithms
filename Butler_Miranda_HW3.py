#HW 3: MSA of stocks 
# [] brackets used to access ELEMENT at defined index


import csv
import math


#import csv file

csvfile = open('HistoricalQuotes.csv')
reader = csv.reader(csvfile)
data = []
data_dates = []
count=0
for row in reader:
	if count==0:
		header = row
	else:
		var = float(row[1])
		data.append(var)
		v2 = row[0]
		data_dates.append(v2)
	count=1

# print data_dates


#make diffeence array
diff = []
end = len(data)
for i in range(0,end):    
	if i==0:
		diff.append(0)
	else:
		var=data[i]-data[i-1]
		diff.append(var)


#MSA algorithm

#Max crossing 
def maxCrossing(A,low,mid,high):
	#define variables
	left_sum= -1000 #-(math.inf) 
	summm = 0
	for i in range(mid,low,-1):          
		summm = summm + A[i]
		if summm > left_sum:
			left_sum = summm
			max_left = i 
			# print 'a'

	right_sum = -1000 #-(math.inf) 
	summm = 0
	for j in range(mid+1,high):
		summm = summm + A[j]
		if summm > right_sum:
			right_sum = summm
			max_right = j
			
	return(max_left,max_right,left_sum+right_sum)


#max left 
def MSAL(A,low,high):
	if high==low:
		return (low,high,A[low]) #fix
	else:
		mid=(low+high)/2
		(left_low,left_high,left_sum) = MSAL(A,low,mid)
		(right_low,right_high,right_sum) = MSAL(A,mid+1,high)
		(cross_low,cross_high,cross_sum) = maxCrossing(A,low,mid,high)

		#? need to define left/right/cross_sum ?do what was done in maxcrossing function again or is it a recursive thing
		if left_sum>=right_sum and left_sum>=cross_sum:
			return (left_low,left_high,left_sum)
		elif right_sum>=left_sum and right_sum>=cross_sum:
			return (right_low,right_high,right_sum)
		else:
			return (cross_low,cross_high,cross_sum)


def MSA(A,low,high):
	if high==low:
		return (low,high,A[low])
	else:
		mid=(low+high)/2
		(left_low,left_high,left_sum) = MSA(A,low,mid)
		(right_low,right_high,right_sum) = MSA(A,mid+1,high)
		
		if left_sum>=right_sum:
			return (left_low,left_high,left_sum)
		else:
			return (right_low,right_high,right_sum)



#call functions
#define inputs
low = 0          
high = len(diff)-1
mid = high/2
A = diff
a = MSA(A,low,high)[2]
b = maxCrossing(A,low,mid,high)[2]


if a>=b:
	print 'max profit'
	print a
	print 'buy date'
	print data_dates[MSA(A,low,high)[0]-1]
	print 'sell date'
	print data_dates[MSA(A,low,high)[1]+1]
else:
	print 'max profit'
	print b
	print 'buy date'
	print data_dates[maxCrossing(A,low,mid,high)[0]-1]
	print 'sell date'
	print data_dates[maxCrossing(A,low,mid,high)[1]+1]


print MSAL(A,low,high) 