#HW: 7
	#Miranda Butler: 100619710

import sys 
import math 


def main(argv):
	#call functions here 
	p =params(argv)
	x = p[0]
	y = p[1]
	areas = p[2]
	prices = p[3]
	profit= []
	tgxyz = []
	t =0 #cut count
	cut(x,y,areas,prices,profit,t,tgxyz)


#---------------------------------------------------------------------------------------------------------------------
# read in parameters 
#---------------------------------------------------------------------------------------------------------------------
def params(argv):
	#read file
 	cloth = []
 	f = open(sys.argv[1], "r")
	
	#write file to list
	for line in f:
		cloth.append(str.strip(line))
	f.close()

	#a_i, b_i, c_i
	products = []
	N = int(cloth[1])
	for i in range(0,N):
		products.append(cloth[i+2])

	#X and Y
	A = cloth[0].split()
	X = int(A[0])
	Y = int(A[1])

	#create array of pattern areas and prices
	areas = []
	prices = []
	Np = len(products)
	for i in range(0,Np):
		temp = products[i].split()
		prices.append(int(temp[0]))
		tempA = int(temp[1])*int(temp[2])
		areas.append(tempA)

	#save to array
	parameters = []
	parameters.append(X)
	parameters.append(Y)
	parameters.append(areas)
	parameters.append(prices)

	return parameters	


def cut(x,y,item_area,item_price,Profit,t,tgxyz):
	#initialize first row 
	Hlength =  x
	fh = [[0]*Hlength for i in range(0,Hlength)]
	Vlength = y
	fv = [[0]*Vlength for i in range(0,Vlength)]
	

	#find max for horizontal
	for i in range(1,len(item_area)):
		for j in range(1,x):
			cut_area = y*j
			if (cut_area-item_area[i])>x or (cut_area-item_area[i])<0: 
				a = 0
			if cut_area > item_area[i]:
				fh[i][j] = max(fh[i-1][j], fh[i-1][a]+item_price[i])
			else:
				if cut_area == item_area[i]:
					fh[i][j] = max(fh[i-1][j], item_price[i])
				else:
					fh[i][j] = fh[i-1][j]
	

	#find max for vertical 
	for i in range(1,len(item_area)):
		for j in range(1,y):
			cut_area = x*j
			if (cut_area-item_area[i])>y or (cut_area-item_area[i])<0: 
				a = 0
			if cut_area > item_area[i]:
				fv[i][j] = max(fv[i-1][j], fv[i-1][a]+item_price[i])
			else:
				if cut_area == item_area[i]:
					fv[i][j] = max(fv[i-1][j], item_price[i])
				else:
					fv[i][j] = fv[i-1][j]

	t=t+1 

#DID NOT FINISH THIS IS MY WORK----------------------------------------------------#
	# #find if veritcal or horizontal is max
	# current_max= max(fh[len(item_area)][x],fv[len(item_area)][y])
	# if current_max==0:
	# 	#if neither cut in half
	# 	x=x/2
	# elif current_max==fh[len(item_area)][x]: #horizontal cut
	# 	Profit.append(current_max*t) #multiply by cut factor
	# 	x= #update rectangle dimension
	# 	g= 
	# 	z=0
	# else: #vertical cut
	# 	Profit.append(current_max*t) 
	# 	y= #update rectangle dimension
	# 	g=
	# 	z=1

	# #update output vals
	# temp = []
	# temp = [t,g,x,y,z] 
	# tgxyz.append(temp)

	#recurse again with new rectangle size
	cut(x,y,item_area,item_price,Profit,t,tgxyz)

	output = []
	output.append(Profit)
	output.append(tgxyz)

	return output




#---------------------------------------------------------------------------------------------------------------------
# main entry point
#---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main(sys.argv)
	
