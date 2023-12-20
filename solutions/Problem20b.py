from aoc_utils import *
from aocd import get_data
from math import lcm


year=2023
day=20

dat = get_data(year=year, day=day, block=True)

modules = [x.replace(' ', '').split('->') for x in parse(dat)]
modules = {m[0][1:]: (m[0][0],  m[1].split(','), False) for m in modules}  # {src: (type, dests[], mem)}

cons = {}

for src, (mtype, dests, _) in modules.items():
    for dest in dests:
        if dest not in cons:
            cons[dest] = {src: False}
        else:
            cons[dest].update({src: False})

presses = 0

first_active = {'xc': False, 'th': False, 'pd': False, 'bp': False}

while True:
    presses += 1
    srcs = [('roadcaster', False)]
    while len(srcs):
        ndests = []
        for src, sig_in in srcs:
            _, cdests, _ = modules[src]
            for d in cdests:
                if d not in modules:
                    if d == 'rx':
                        if sig_in:
                            for prev in first_active:
                                if cons['zh'][prev] and not first_active[prev]:
                                    first_active[prev] = presses

                            if all(first_active.values()):
                                print(first_active)
                                print(lcm(*first_active.values()))
                                exit()
                    continue
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
