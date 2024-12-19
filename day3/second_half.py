import re

def proc_mul(cmd):
    l = [int(n) for n in cmd[4:-1].split(",")]
    return l[0] * l[1]

mul_pattern = re.compile(r"mul\(-*\d+,-*\d+\)")
do_pattern = re.compile(r"don*'*t*\(\)")

with open("input.txt", 'r') as f:
    inpt_ = f.readlines()

inpt = "".join(inpt_)

matched_mul = []
matched_do = []

for m in mul_pattern.finditer(inpt):
    s_idx, e_idx = m.span()
    matched_mul.append((inpt[s_idx: e_idx], s_idx))

for m in do_pattern.finditer(inpt):
    s_idx, e_idx = m.span()
    matched_do.append((inpt[s_idx: e_idx], s_idx))

do_idx = 0
do_flag = True
v = 0
for idx in range(len(matched_mul)):
    m_idx = matched_mul[idx][1]
    if do_idx < len(matched_do):
        d_idx = matched_do[do_idx][1]
        if m_idx > d_idx:
            do_cmd = matched_do[do_idx][0]
            if do_cmd == "do()":
                do_flag = True
            else:
                do_flag = False
            do_idx += 1
    
    if do_flag:
        v += proc_mul(matched_mul[idx][0])

print(v)
