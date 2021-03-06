# Matthew Tan
# mxtan@ucsc.edu
# pa3
# Primes.py

def isPrime(m, L):
    while True:
        for p in L:
            if m < p**2:
                return True
                break
            if m % p == 0:
                return False
                break
#-- main program ---------------------------------------------------------   
print("")
n = int(input("Enter the number of Primes to compute: "))
PrimeList = [2]

m = 2
while True:
    listLength = len(PrimeList)
    if isPrime(m, PrimeList) == True and m != 2:
        PrimeList.append(m)
    if listLength == n:
        break
    m += 1

print(" ")
print("The first", n, "primes are: ", end="")
for i in range(len(PrimeList)):
    if i % 10 == 0:
       print(" ")
    print(PrimeList[i], end= " ")
print("\n")
