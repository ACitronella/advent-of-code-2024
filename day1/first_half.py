with open("input.txt", 'r') as f:
    inpt = f.readlines()

d = [l.split('   ') for l in inpt]
d = [(int(a), int(b)) for a, b in d]
l = [a for a, b in d]
r = [b for a, b in d]

l = sorted(l)
r = sorted(r)

print(sum([abs(li - ri) for li, ri in zip(l, r)]))
