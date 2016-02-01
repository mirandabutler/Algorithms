#HW 2: RSA enrytion and decryption 
# Miranda Butler: 100619710 

#import  
from random import randint
import timeit

#generate list of primes 
def primes_sieve(n):
    nn = n+1
    not_prime = [False] * nn  # [0]*nn
    primes = []

    for i in range(2, nn):
        if not_prime[i]:
            continue
        for f in range(i*2, nn, i): #start,stop,step
            not_prime[f] = True

        primes.append(i)

    return primes


def euclid(a, b):
	if b == 0: 
		return a
	
	return euclid(b, a%b)


def extendedEuclid(a, b):
	if b == 0: 
		return (1, 0, a)
	(xp, yp, d) = extendedEuclid(b, a%b)
	
	return (yp, xp-(a/b)*yp, d)


def keys():
	start = timeit.default_timer()
#select 2 large primes 
	n = len(primes)
	rand1 = randint(0,n-1) 
	rand2 = randint(0,n-1) 
	p = primes[rand1]
	q = primes[rand2]

#define variables
	N = p*q
	phi = (q-1)*(p-1) 


#Public Key: e 
	#e is prime, [3,phi], gcd(e,phi==1)
	for i in range(n-1,0,-1):
		e=primes[i]
		if (3<=e<phi) and euclid(e,phi)==1:
			break

#Private Key: d
	#d is prime, e*d=1(mod phi) --> d*e-k*phi=1 --> 1 = x'*e + y'*phi, where x'=d and y'=-k 
	d = extendedEuclid(e,phi)[0]

	stop = timeit.default_timer()
	time = stop-start
	return (e,d,N,time)


#Encryption: C
def RSAencrypt(e,M,N):
	start = timeit.default_timer()
	C = (M^e)%N
	stop = timeit.default_timer()
	time = stop-start
	return (C,time)

#Decryption: M
def RSAdecrypt(d,C,N):
	start = timeit.default_timer()
	M = (C^d)%N
	stop = timeit.default_timer()
	time = stop-start
	return (M,time) 


#Define variables
n=10^9 # 8bit n=1000, 16 bit n=10000, 32bit n=10^10 (3,5,10)  
primes = primes_sieve(n) #array of primes
M = 55 #message



N= keys()[2]
e = keys()[0]
d=keys()[1]


#call functions 
print "encryted message"
C = RSAencrypt(e,M,N)[0]
print C

print "decrypted message"
newM = RSAdecrypt(d,C,N)[0]
print newM

print "run time for keys "
print keys()[3]

print "run time for encrytion"
print RSAencrypt(e,M,N)[1]

print "run time for decryption"
print RSAdecrypt(d,C,N)[1]


