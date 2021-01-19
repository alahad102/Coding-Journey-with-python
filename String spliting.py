
t = int(input())
i = 0
d =[]
while (i<t):
    s1 = input()
    i = i+1
    d.append(s1)

for i in range(len(d)):
    s = d[i]

    j=0
    while j<(len(s)):
        print(s[j], end ="")
        j= j+2
    print(" ", end ="")

    k = 1
    while k<len(s):
        print(s[k], end="")
        k=k+2
    print()