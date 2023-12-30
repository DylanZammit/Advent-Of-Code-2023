# Advent of Code 2023

Attempts for the [Advent of Code](https://adventofcode.com/).

## [Problem 1](https://adventofcode.com/2023/day/1)
### Part 1
Part 1 is simple since it is only required to find the first digit and its index using

`i1, d1 = next((i, d) for i, d in enumerate(row) if d in digits).`

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

`found = any([re.search(r'[^\d|\\.]', data[i-z][start:end]) for z in [-1, 0, 1]]).`

We iterate each row and within each row, we iterate through all numbers. For instance we would iterate the row `....325....76...` once for `325` and once for `76`. For each iteration we check all adjacent symbols using the above code. The regex `[^\d|\\.]` matches non-numbers and non-periods, which only leaves  `*`.  

### Part 2
Part  2 is slightly more involved but ultimately the same concept. We also keep track of the number of adjacent numbers to cogs, since we only care about cogs with 2 adjacent numbers. 
## [Problem 4](https://adventofcode.com/2023/day/4)
After parsing the input data for part 1, the code is essentially the sum of the values of this line:

`sum(int(2**(len(v['winning'].intersection(v['showing']))-1)) for k, v in input.values())`
## [Problem 5](https://adventofcode.com/2023/day/5)
### Part 1
Part 1 is small enough to brute force by storing the srouce/destination ranges. For a particular source, we can then find the correct destination by running

`next((d + (val - s) for d, s, r in maps[dest] if s <= val < s + r), val)`

This searches the list of ranges until the given source (val) is within the specified range. We then return the offset of the start of the destination range and the value.
### Part 2
An implementation such as the above is _not_ possible as the mapping is far too large. We need to generalise the same idea by using ranges instead of single points.
To do this, we define a function `get_loc` accepting the start/end of each range, and then splitting this range into smaller sub-ranges and calling `get_loc` for these smaller sub-ranges. The magic happens in this snippet
```
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

`r=(t-p)p => p^2-tp+r=0 => p_record = (t + sqrt(t^2 - 4r)) / 2`.

We notice that this is a quadratic equation, so the possible range of improvements occur at points around the optimal point `p_opt` up until `p_record`.
In the below example, each `.` represents a millisecond pressed, `v` represents `p_opt` and `r` represents `p_record`. The values in the bracket represent the possible improvemenets.

`.....(..v..)r....`
### Part 2
The same implementation as the above can be used.
## [Problem 7](https://adventofcode.com/2023/day/7)
### Part 1
There are two things to take care of:
* The first order of ranking is determined by the number of unique cards contained. This can be hardcoded in an array, where the index is the ranking. Having `AAAAK` gives a Counter of `{'A': 4, 'K': 1}`. We then take a list of the counts: `[4, 1]` which has the second highest rank in the following array (4-of-a-kind).

`ranks = [[5], [1, 4], [2, 3], [1, 1, 3], [1, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1, 1]]`
* If two cards have the same rank, the first card from the left-side of the hand having the highest value will be the dominant one. Since there are a total of `13` possible cards, we treat it as a base `13` number, and we simply order tied ranks by its base 13 value.

`sum([cards[h] * 13 ** i for i, h in enumerate(hand[::-1])])`

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

```
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
## [Problem 13](https://adventofcode.com/2023/day/13)
## [Problem 14](https://adventofcode.com/2023/day/14)
## [Problem 15](https://adventofcode.com/2023/day/15)
## [Problem 16](https://adventofcode.com/2023/day/16)

A dynamic programming, depth-first approach was taken to solve this problem. Whenever a split occurs, i.e. a horizontal beam collides with a | mirror, or a vertical beam collides with a - mirror, then the function is recursed twice for both beams. (Video illustration below)

[![Advent Of Code Problem 16](https://img.youtube.com/vi/r74SKH55auo/0.jpg)](https://www.youtube.com/watch?v=r74SKH55auo)

## [Problem 17](https://adventofcode.com/2023/day/17)

An application of Djikstra's pathfinding algorithm was used, where the state space is in the form of (position, direction).

![Advent Of Code Problem 17](https://github.com/DylanZammit/Advent-Of-Code-2023/blob/master/img/problem17_vis.png?raw=true)

## [Problem 17](https://adventofcode.com/2023/day/17)
## [Problem 18](https://adventofcode.com/2023/day/18)
## [Problem 19](https://adventofcode.com/2023/day/19)
## [Problem 20](https://adventofcode.com/2023/day/20)
## [Problem 21](https://adventofcode.com/2023/day/21)
## [Problem 22](https://adventofcode.com/2023/day/22)
## [Problem 23](https://adventofcode.com/2023/day/23)
## [Problem 24](https://adventofcode.com/2023/day/24)
## [Problem 25](https://adventofcode.com/2023/day/25)
