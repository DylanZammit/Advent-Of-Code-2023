# Advent of Code 2023

Attempts for the [Advent of Code](https://adventofcode.com/) 2023.

![Advent Of Code Problem 21](https://github.com/DylanZammit/Advent-Of-Code-2023/blob/master/img/calendar.png?raw=true)

**WARNING: SPOILERS AHEAD**

## [Problem 1](https://adventofcode.com/2023/day/1)
### Part 1
Part 1 is simple since it is only required to find the first digit and its index using

```python
i1, d1 = next((i, d) for i, d in enumerate(row) if d in digits)
```

The last digit and index `i2, d2` are also found by reversing the string `row[::-1]`. Then we check if `i1 == i2`, indicating that the digit is the same, and should **not** be double counted.

### Part 2
Part 2 is a rather convoluted way to replace the first occurrence of number in word-form to a digit. Care needs to be taken for cases such as `eightwo`. 
## [Problem 2](https://adventofcode.com/2023/day/2)
### Part 1
If there is at least one R, G, B count greater than their respective maximum, then the game is impossible.
### Part 2
The trick here is taking the `maxmin` of the showings. The minimum number of red balls, is the maximum of their occurrences in all games.
## [Problem 3](https://adventofcode.com/2023/day/3)
### Part 1
Part 1 is easily solvable by using regex with

```python
found = any([re.search(r'[^\d|\\.]', data[i-z][start:end]) for z in [-1, 0, 1]])
```

We iterate each row and within each row, we iterate through all numbers. For instance we would iterate the row `....325....76...` once for `325` and once for `76`. For each iteration we check all adjacent symbols using the above code. The regex `[^\d|\\.]` matches non-numbers and non-periods, which only leaves  `*`.  

### Part 2
Part  2 is slightly more involved but ultimately the same concept. We also keep track of the number of adjacent numbers to cogs, since we only care about cogs with 2 adjacent numbers. 
## [Problem 4](https://adventofcode.com/2023/day/4)
After parsing the input data for part 1, the code is essentially the sum of the values of this line:

```python
sum(int(2**(len(v['winning'].intersection(v['showing']))-1)) for k, v in input.values())
```
## [Problem 5](https://adventofcode.com/2023/day/5)
### Part 1
Part 1 is small enough to brute force by storing the srouce/destination ranges. For a particular source, we can then find the correct destination by running

```python
next((d + (val - s) for d, s, r in maps[dest] if s <= val < s + r), val)
```

This searches the list of ranges until the given source (val) is within the specified range. We then return the offset of the start of the destination range and the value.
### Part 2
An implementation such as the above is _not_ possible as the mapping is far too large. We need to generalise the same idea by using ranges instead of single points.
To do this, we define a function `get_loc` accepting the start/end of each range, and then splitting this range into smaller sub-ranges and calling `get_loc` for these smaller sub-ranges. The magic happens in this snippet
```python
def get_loc(src, start, end, n=1):
    if src == 'location': return start
    dest = from_to[src]

    gg = []
    ss = start
    while ss <= end:
        s, e = get_map(dest, ss, end)
        gg.append(get_loc(dest, s, e, n+1))
        ss += e - s + 1
    return min(gg)
```
## [Problem 6](https://adventofcode.com/2023/day/6)
### Part 1
If we press the button for `p` milliseconds, the distance travelled in `t` seconds is `d=(t-p)p`. 
We can optimise `d` by differentiating, equating to zero and solving for `p`, giving us `p_opt=t/2`.
We also need to find the original number of milliseconds pressed for the current record `r`. 
We can solve for `p` in the equation 

`r=(t-p)p => p^2-tp+r=0 => p_record = (t + sqrt(t^2 - 4r)) / 2.`

We notice that this is a quadratic equation, so the possible range of improvements occur at points around the optimal point `p_opt` up until `p_record`.
In the below example, each `.` represents a millisecond pressed, `v` represents `p_opt` and `r` represents `p_record`. The values in the bracket represent the possible improvemenets.

`.....(..v..)r....`
### Part 2
The same implementation as the above can be used.
## [Problem 7](https://adventofcode.com/2023/day/7)
### Part 1
There are two things to take care of:
* The first order of ranking is determined by the number of unique cards contained. This can be hardcoded in an array, where the index is the ranking. Having `AAAAK` gives a Counter of `{'A': 4, 'K': 1}`. We then take a list of the counts: `[4, 1]` which has the second highest rank in the following array (4-of-a-kind).

```python
ranks = [[5], [1, 4], [2, 3], [1, 1, 3], [1, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1, 1]]
```
* If two cards have the same rank, the first card from the left-side of the hand having the highest value will be the dominant one. Since there are a total of `13` possible cards, we treat it as a base `13` number, and we simply order tied ranks by its base 13 value.

```python
sum([cards[h] * 13 ** i for i, h in enumerate(hand[::-1])])
```

### Part 2
For a hand with such a rank `{X: n1, Y: n2, J: n3}`, we find the key corresponding to the largest value `ni`, and convert all `J`s to that value. We then run the same algorithm as part 1.

Ex. `{Q: 1, 5: 3, J: 1} -> {Q: 1, 5: 4}`
## [Problem 8](https://adventofcode.com/2023/day/8)
### Part 1
Created a map of the input and followed the instructions given by the problem.
### Part 2
## [Problem 9](https://adventofcode.com/2023/day/9)
### Part 1
Probably my proudest implementation. We create a function `get_diff` which accepts an array of integers. This function computes the diff of this sequence of numbers, and calls itself with the new differenced list. This process is repeated until the inpuuted list contains at least one zero. The whole implementation is four lines of code!

```python
def get_diff(seq):
    out = np.diff(seq)
    return seq[-1] + (get_diff(out) if any(out) else 0)

print(sum([get_diff(row) for row in dat]))
```
### Part 2
The same implementation as above, but simply replacing `seq[-1]` with `seq[0]` to start from the beginning instead of the end, and subtract the difference instead of adding it.
## [Problem 10](https://adventofcode.com/2023/day/10)
### Part 1
Start from `S` and simply check the direction of the adjacent pipe which has the correct configuration. Repeat this process until we return to `S`, counting the steps as we go. The furthest point is half the number of steps.
### Part 2
Start from the left-most part of the map, and cut a horizontal line to the other side of the map, counting the number of pipe-cuts as you go. For a point to be inside the loop, there must be an odd parity of pipes-cut. 
Pipes of the form `F---7` and `L---J` can be considered as two (or zero) vertical pipes `||`, while "S" shaped pipes such as `F---J` or `L---7` can be considered as a single pipe `|`.

**NOTE**: Problem 18 is of a similar nature to this, which is much harder. The [Shoelace Formula](https://en.wikipedia.org/wiki/Shoelace_formula) and [Pick's Theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem) were used to solve this problem instead, which is much simpler, faster and elegant. A more detailed explanation is given there.
## [Problem 11](https://adventofcode.com/2023/day/11)
### Part 1
This is essentially the `l1` distance (or the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry)), i.e. summing the vertical and horizontal distances together. We simply calculate the sum of all such pair of distances, having complexity of `O(n^2)` where `n` is the number of galaxies.
### Part 2
The exact same implementation can be used, where we multiply the distances by `m = 1_000_000 - 1`.
## [Problem 12](https://adventofcode.com/2023/day/12)
Jesus, Mary mother of God this took me a while.

In very very loose terms: a dynamic programming approach was used where we find the next `#` or `?`, count the possibilities at this point, and repeat the procedure for the next occurrence. 
## [Problem 13](https://adventofcode.com/2023/day/13)
### Part 1
Iterate each row and check if that is the point of reflection by expanding outward, and checking that the rows are the same as we move out. For example if we are comparing row 4, we check rows (3, 4), (2, 5), (1, 6) etc until we run out of lines. We return the index of this line of reflection. To check for the opposite direction, we simplly transpose the matrix and repeat.
### Part 2 
We amend the above logic by starting off with a `smudge=False` indicator. We perform the same procedure, but instead of checking whether two lines are exactly the same, we use [Hamming Distance](https://en.wikipedia.org/wiki/Hamming_distance) instead. 

If this distance is greater than 1, there are too many smudges. If it is exactly equal to 0, we proceed since the lines are identical. If the distance is 1, and smudge is False, we can set `smudge` to `True` and proceed with the same algorithm. This essentially gives a "free pass" for exactly one smudge. 
## [Problem 14](https://adventofcode.com/2023/day/14)
### Part 1
Happy with my implementation of part 1, even though it will bite me for the second part. I do not actually create an array and move all rocks, instead I 
* Transpose the input to search horizontally
* search for the next `O` occurrence in the
* find the first of an `#` or EOL occurrence from this `O` and consider the distance `d`,
* count the number of `O`s in that substring `m`
* the `O`s new position will move by an amount of `d-m`.

The whole code is given by
```python
out, n = 0, len(dat[0])
for r in dat:
    for z in re.finditer(r'O', r):
        m = re.match(rf'.{{{z.start()}}}[O.]*((?=#)|$)', r)
        out += m.end() - m.string[z.start() + 1:m.end()].count('O') if m else 0

print(out)
```
### Part 2
Unfortunately, the code for part 1 does not generalise at all for part 2, and we _actually_ have to find the position of the new stones. We do this procedure, iterate, and print the output at every step. At some point, we notice a cycle of length `C` starts at some point `N`. Let `M` be the number of cycles provided in the example. Then our solution would be at the `(M - N) % C`th position of this sequence. I have not implemented this part of the problem in python neatly yet, and only did it manually by the Ctrl+F algorithm (yuck). 
## [Problem 15](https://adventofcode.com/2023/day/15)
### Part 1
We just follow the steps provided in the problem by creating the below hashing function.
```python
def hasher(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res
```
### Part 2
Another straightforward implementation, that utilises the above function.
```python
hm = {i: {} for i in range(256)}

for s in dat.split(','):
    if '-' in s:
        ss = s[:-1]
        hm[hasher(ss)].pop(ss, None)
    else:
        ss, val = s.split('=')
        hm[hasher(ss)][ss] = val

print(sum((k+1) * (i+1) * int(fl) for k, v in hm.items() for i, (ss, fl) in enumerate(v.items())))
```
## [Problem 16](https://adventofcode.com/2023/day/16)

A dynamic programming, depth-first approach was taken to solve this problem. Whenever a split occurs, i.e. a horizontal beam collides with a | mirror, or a vertical beam collides with a - mirror, then the function is recursed twice for both beams. (Video illustration below)

[![Advent Of Code Problem 16](https://img.youtube.com/vi/r74SKH55auo/0.jpg)](https://www.youtube.com/watch?v=r74SKH55auo)

## [Problem 17](https://adventofcode.com/2023/day/17)

An application of Djikstra's pathfinding algorithm was used, where the state space is in the form of (position, direction).

![Advent Of Code Problem 17](https://github.com/DylanZammit/Advent-Of-Code-2023/blob/master/img/problem17_vis.png?raw=true)

## [Problem 18](https://adventofcode.com/2023/day/18)
### Part 1
A brute force approach was taken, where we literally count the number of cubes inside the boundary, using a similar method as Day 10's.
### Part 2
A brute force approach fails miserable here. The [Shoelace Formula](https://en.wikipedia.org/wiki/Shoelace_formula) and [Pick's Theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem) were used to solve this problem instead, which is much simpler, faster and elegant.

* The **Shoelace formula** takes each successive vertex coordinates `(x1, y1)` and `(x2, y2)` and calculates the determinant of the two. The sum of all these determinants is summed together until a cycle is formed. Dividing the value by 2 gives the area of the polygon.
* **Pick's Theorem** gives a formula for the area of a polygon given the number of integer coordinates on the boundary (`b`) and the interior (`i`). This is given by `A=i+b/2-1`.
* After finding `A` from the Shoelace formula, and finding `b` by summing the lengths of the given input, we can find `i` by using subject of the formula of Pick's Theorem, giving us the answer.
## [Problem 19](https://adventofcode.com/2023/day/19)
### Part 1
A mapping is created according to the given input, and a brute force procedure is created as per the instructions.
### Part 2
Part 1's solution does not work for part 2. We apply a similar approach as that of Day 5's, where we create a recursive function, and count the valid inputs by splitting the initial ranges into smaller sub-ranges, and call the same function with these sub-ranges separately.
## [Problem 20](https://adventofcode.com/2023/day/20)
### Part 1
Similar to the above, we simply follow the procedure stated by the problem to get the correct result.
### Part 2
Once again, the above is not viable. Creating a generalised solution is also not easy, however, taking a closer look at the input data, we notice something interesting. The `rx` node is preceded by a single `zh` node, and in turn called by four conjunction modules. For this flag to send a low pulse, all four flags need to be set to have a low-pulse memory.

We count the number of iterations needed for each one to be set to 1, and we notice that these happen in a cycle! Suppose that module `i` (where `i=1,2,3 or 4`) is set to 1 every `ni` iterations. Then these flags are all set to `1` every `lcm(n1, n2, n3, n4)` iterations, giving us the solution.

NOTE: It is NOT obvious why LCM should work here because we have no guarantee that the cycle will remain the same ad infinitum, but hey, it works.
## [Problem 21](https://adventofcode.com/2023/day/21)
### Part 1
A brute force solution was implemented to get the correct result.
![Advent Of Code Problem 21](https://github.com/DylanZammit/Advent-Of-Code-2023/blob/master/img/problem21_vis.png?raw=true)
### Part 2
Looking at the output of Part 1 and the problem of Part 2 closely we notice some interesting things.
* The centre of the input is a diamond shape
* The corners of the input are quarters of diamonds, meaning that tiling the inputs gives many adjacent diamonds.
* The final stones after 64 steps are alternating
* Taking `26501365 % 131` gives exactly `65`, where `131` is the width/height of the input.

This indicates that there is a pattern in the output. The result of the modulo hints that a pattern might emerge if we ignore the iteration of the first tile.

Initially I tried coming up with an equation manually, where I noticed that the solution is quadratic in the number of steps.  Finally, I let the script fo Part 1 run to give me the results of `65`, `65 + 131 * 1` and `65 + 131 * 2` steps. This gives me 3 points on the quadratic. I unapologetically asked [WolframAlpha](https://www.wolframalpha.com/) to give me the quadratic passing through the given points. This gives me a quadratic given by
```python
def res(s): return (14860 * s ** 2)/17161 + (23375 * s)/17161 + 256807/17161
```
I then simply fed the number of steps `26501365 = 131 * 202300 + 65` into this formula to get the answer.
## [Problem 22](https://adventofcode.com/2023/day/22)
### Part 1
I create a mapping where each block has its supports as parents (and vice versa). To do this I
* create an array of "settled" blocks (initialised as empty)
* iterate over the blocks sorted by the lowest `z` coordinate
* for each such block, I check if there is an `x` overlap and `y` overlap between each settled block.
* Once such a block is found, I add the support to the map
* Once this mapping is created, I count the number of blocks having only one support.
### Part 2
We can amend the above implementation, to count the largest chain of supports for each non-disintegratable block.
## [Problem 23](https://adventofcode.com/2023/day/23)
### Part 1
Used DFS, recursing on itself once a junction is reached. The hills `>` form a DAG, making this easy to solve. 

Dijkstra could also have been used with negative weights since there are no negative weighted cycles (due to the hills).
### Part 2
Removing `>` gives a much harder problem, in fact it is `NP-hard`. We form a graph, where each node is a junction, and the weight of the edges are the distance between two nodes. We can again use DFS to search for the longest path. The graph is small enough for this to work.
## [Problem 24](https://adventofcode.com/2023/day/24)
### Part 1
We compare each two lines together and if the two lines are not parallel, we can find the [point of intersection](https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_line_equations). We take the vector from this point to the starting point of the line, and only count it as an intersection if it is not in the opposite direction of the velocity vector. This means that the intersection can only happen in the future.
### Part 2
We need to create a set of equations and solve them. Let `l` be the line we need to find, having `p` as the initial position `v` its velocity vector. Let all other lines in the input be denoted by `l1`, `l2`, ..., `ln` each having position and velocity vectors `pi` and `vi` respectively.

The set of equations we need to solve are

```
p+t1*v=p1+t1*v1
p+t2*v=p2+t2*v2
p+t3*v=p3+t3*v3
...
p+tn*v=pn+tn*vn
```
The unknown variables are thus `px, py, pz, vx, vy, vz, t1, t2, ..., tn`, noting that `p` and `v` are 3-D vectors. In total there are `n+6` unknown variables.

Do we need all lines to find the solution? We simply need there to be more lines than there are unknown variables. Since each line creates 3 new equations, we have

```3n >= n+6    =>    n >= 3```

Thus, 3 lines are enough to give us the solution, giving us only 9 equations and 9 unknown variables! The use of `sympy` was used to solve these equations.
## [Problem 25](https://adventofcode.com/2023/day/25)
### Part 1
We use a Monte Carlo algorithm called [Karger's min-cut algorithm](https://en.wikipedia.org/wiki/Karger%27s_algorithm). This algorithm works by randomly contracting vertices and edges, until the graph has exactly two supervertices. We take note of the number of vertices merged on each iteration. We can repeat this algorithm multiple times until it gives us a cut of size 3 (which happens almost immediately). When this happens, we simply take the number of merges of the two vertices, and multiple together to get the answer!

The algorithm was blatantly copy and pasted (and amended for my use) from the top solution of [this StackOverflow question](https://stackoverflow.com/questions/23825200/karger-min-cut-algorithm-in-python-2-7).

[This document](https://web.stanford.edu/class/archive/cs/cs161/cs161.1172/CS161Lecture16.pdf) was used to understand the algorithm better.
### Part 2
Pressed the big red button!