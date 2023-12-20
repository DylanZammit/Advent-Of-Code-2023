from aoc_utils import *
from aocd import get_data
import regex as re
import numpy as np

year=2023
day=20

dat = get_data(year=year, day=day, block=True)

# 11687500
dat1 = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output'''

# 32000000
dat2 = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''

modules = [x.replace(' ', '').split('->') for x in parse(dat)]
modules = {m[0][1:]: (m[0][0],  m[1].split(','), False) for m in modules}  # {src: (type, dests[], mem)}

cons = {}

for src, (mtype, dests, _) in modules.items():
    for dest in dests:
        if dest not in cons:
            cons[dest] = {src: False}
        else:
            cons[dest].update({src: False})

lct = 1000
hct = 0
for i in range(1000):
    srcs = [('roadcaster', False)]
    while len(srcs):
        ndests = []
        for src, sig_in in srcs:
            _, cdests, _ = modules[src]
            for d in cdests:
                if sig_in:
                    hct += 1
                else:
                    lct += 1
                if d not in modules: continue
                mtype, cdests, mem = modules[d]
                end = False
                if mtype == '%':
                    if not sig_in:
                        sig_out = not mem
                        modules[d] = (mtype, cdests, sig_out)
                    else:
                        end = True
                elif mtype == '&':
                    cons[d][src] = sig_in
                    sig_out = not all(z for _, z in cons[d].items())
                else:
                    sig_out = sig_in  # broadcast

                if not end:
                    ndests.append((d, sig_out))

        srcs = ndests
out = lct * hct

print(out)

