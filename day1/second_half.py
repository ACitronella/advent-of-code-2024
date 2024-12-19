
with open("input.txt", 'r') as f:
    inpt = f.readlines()

d = [l.split('   ') for l in inpt]
d = [(int(a), int(b)) for a, b in d]
l = [a for a, b in d]
r = [b for a, b in d]
c = {}
for ri in r:
    if ri in c:
        c[ri] += 1
    else:
        c[ri] = 1

s = 0
for li in l:
    if li in c:
        s += li * c[li]   

print(s)
