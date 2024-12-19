import re

def proc_mul(cmd):
    l = [int(n) for n in cmd[4:-1].split(",")]
    return l[0] * l[1]

pattern = re.compile(r"mul\(-*\d+,-*\d+\)")

with open("input.txt", 'r') as f:
    inpt_ = f.readlines()

inpt = "".join(inpt_)

print(sum([proc_mul(cmd) for cmd in pattern.findall(inpt)]))