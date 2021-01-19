
e = { }
t = int(input())
for i in range(t):
    k, v = input().split()
    e.update({k:v})
while True:
    try:
        q = input()
        if q in e:
            print(q + "=" + e[q])
        else:
            print("Not found")
    except:
        break


