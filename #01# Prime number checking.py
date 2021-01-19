
from math import floor
x = int(input("Enter a number whether it is prime or not:"))

for i in range(2,floor(x/2)):
    if x % i == 0:
        print("Not prime")
        break
else:
    print("prime")